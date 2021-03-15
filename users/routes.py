
from flask import Blueprint, render_template
from users.forms import LoginForm

users = Blueprint('users', __name__)


@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('users/login.html', form=form)


@users.route('/register')
def register():
    return 'register page'
