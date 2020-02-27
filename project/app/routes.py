from app import app
from app.forms import LoginForm
from flask import render_template,flash,redirect

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
@app.route('/<name>')
def hello_name(name):
    return "Hello {} xd!".format(name)
