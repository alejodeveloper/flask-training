import unittest

from flask import request, make_response, redirect, render_template, session, url_for
from flask_login import login_required, current_user

from app.app import create_app

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('not_found.html', error=error)


@app.route("/")
def index():
    response = make_response(redirect(url_for('hello')))
    session['user_ip'] = request.remote_addr

    return "Hello"


@app.route("/hello")
def hello():
    context = {
        'user_ip': session.get('user_ip'),
        'todos': [],
        'username': current_user.id,
    }
    return "Hello"
