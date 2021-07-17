from flask import Blueprint, render_template
from users.models import User


admin = Blueprint('admin', __name__)


@admin.route('/administrator')
def administrator():
    context = {
        'users': 'this is users query',
    }
    return render_template('admin/administrator.html', context=context)


@admin.route('/usersInfo')
def users():
    users = User.query.all()
    return render_template('admin/usersInfo.html', users=users)
