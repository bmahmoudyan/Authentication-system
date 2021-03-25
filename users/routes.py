
from flask import Blueprint, render_template
from users.forms import LoginForm, RegisterForm

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
    return render_template('users/register.html', form=form)
