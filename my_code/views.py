from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from my_code.models import Case, Custodian
from flask.ext.mongoengine.wtf import model_form

#cases = Blueprint('cases', __name__, template_folder='templates')

#class CaseView(MethodView):

#	def get(self):
#		cases = Case.objects.all()
#		return render_template('admin/admin.html', cases=cases)


#cases.add_url_rule('/', view_func=ListView.as_view('case'))