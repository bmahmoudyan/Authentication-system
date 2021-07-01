
from app import db


class User(db.Model):
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
        return f'{id}, {self.name}, {self.username}, {self.email_addr}:{self.email_addr_is_Confirm}, {self.phone_number}:{self.phone_number_is_Confirm}'
