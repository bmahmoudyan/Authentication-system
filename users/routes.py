
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/login')
def login_view():
    return 'login page'


@users.route('/register')
def register_view():
    return 'register page'
