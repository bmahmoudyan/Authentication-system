from flask import Blueprint, render_template


admin = Blueprint('admin', __name__)


@admin.route('/administrator')
def administrator():
    context = {
        'users': 'this is users query',
    }
    return render_template('admin/administrator.html', context=context)
