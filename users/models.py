
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(180), nullable=False, unique=True)
    email_is_Confirm = db.Column(db.Boolean, nullable=True)
    phone_number = db.Column(db.String(80), nullable=False, unique=True)
    phone_number_is_Confirm = db.Column(db.Boolean, nullable=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{id}, {self.username}, {self.email}'


class UserConfirmCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    code = db.Column(db.String(6))
