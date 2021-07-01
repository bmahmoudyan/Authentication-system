from app import db
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from users.forms import LoginForm, RegisterForm
from users.models import User

users = Blueprint('users', __name__)


@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('login successful')
    return render_template('users/login.html', form=form)


@users.route('/logout')
def logout():
    print('log out user')


@users.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('register is validate_on_submit')
        new_user = User(name=form.name.data, last_name=form.last_name.data, username=form.username.data,
                        email=form.email.data, phone_number=form.phone_number.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/register.html', form=form)
