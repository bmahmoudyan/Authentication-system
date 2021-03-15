
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/login')
def login_view():
    return 'login page'
