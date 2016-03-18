from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

##from tumblelog.auth import requires_auth
from my_code.models import Case, Custodian

admin = Blueprint('admin', __name__, template_folder='templates')


class Cases(MethodView):
    #decorators = [requires_auth]
    #Set the class that will be passed into the mongodb query
    cls = Case

    def get(self):
    	#get all the cases in the db
        cases = self.cls.objects.all()
        return render_template('admin/admin.html', cases=cases)


class CaseDetail(MethodView):


	def get_context(self, slug=None):
		form_cls = model_form(Case, exclude=['created_at'])
		if slug:
			case = Case.objects.get_or_404(slug=slug)
			if request.method == 'POST':
				form = form_cls(request.form, inital=case._data)
			else:
				form = form_cls(obj=case)
		else:
			case = Case()
			form = form_cls(request.form)

		context = {
            "case": case,
            "form": form,
            "create": slug is None}
		return context

	def get(self, slug):
		context = self.get_context(slug)
		return render_template('admin/case.html', **context)

	def post(self, slug):
		context = self.get_context(slug)
		form = context.get('form')

		if form.validate():
			case = context.get('case')
			form.populate_obj(case)
			case.save()

			return redirect(url_for('admin.index'))
		return render_template('admin/case.html')

admin.add_url_rule('/admin/', view_func=Cases.as_view('index'))
admin.add_url_rule('/admin/create/', defaults={'slug': None}, view_func=CaseDetail.as_view('create'))
admin.add_url_rule('/admin/<slug>/', view_func=CaseDetail.as_view('edit'))

