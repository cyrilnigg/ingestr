# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask import render_template, request, redirect, url_for
from my_code import app

manager = Manager(app)

#@app.route('/admin')
#def admin_page():
#	return render_template('admin/admin.html')

@app.route('/admin/create-case')
def create_case():
	return render_template('admin/create-case.html')

@app.route('/admin/case_name')
def view_case():
	return "view case"

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()