from app import db
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from users.forms import LoginForm, RegisterForm
from users.models import User

users = Blueprint('users', __name__)


@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return redirect(url_for('main.home'))
    return render_template('users/login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, last_name=form.last_name.data, username=form.username.data,
                        email=form.email.data, phone_number=form.phone_number.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/register.html', form=form)


@users.route('/user/<string:username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/userProfile.html', context=user)


# TODO confirm user phone number
@users.route('/confirmPhoneNumber')
def confirm_phone_number():
    return render_template('users/confirmPhoneNumber.html')


# TODO confirm user email address