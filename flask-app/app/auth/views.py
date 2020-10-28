from flask import render_template, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from .blueprint import auth_blueprint
from app.forms import LoginForm
from app.firestore_service import get_user, create_user
from app.models import UserData, UserModel


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.username.data

        user_doc = get_user(username)
        if user_doc.to_dict():
            password_doc = user_doc.to_dict().get('password')
            if password_doc == password:
                user_data = UserData(username=username, password=password)
                user = UserModel(user_data)

                login_user(user)
                flash("Welcome Back")
                return redirect(url_for('hello'))
            else:
                flash("User doesn't exists")
        else:
            flash("User doesn't exists")

        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth_blueprint.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        user_doc = get_user(username)
        if not user_doc.to_dict():
            password_hash = generate_password_hash(signup_form.password.data)
            user_data = UserData(username=username, password=password_hash)
            create_user(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash('Welcome')
            return redirect(url_for('index'))
        else:
            flash('User already exists')

    return render_template('signup.html', **context)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('come back soon!')

    return redirect(url_for('auth.login'))
