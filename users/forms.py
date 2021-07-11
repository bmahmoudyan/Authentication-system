from flask_wtf import FlaskForm
from users.models import User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()],  render_kw={
        "placeholder": "username", 'id': 'inputEmail4'})
    password = PasswordField(' password', validators=[DataRequired()],  render_kw={
                             "placeholder": "password", 'id': 'inputPassword4'})
    submit = SubmitField(
        render_kw={"value": "LOGIN"})


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)], render_kw={
                       "placeholder": "enter your name", 'id': 'inputEmail4'})

    last_name = StringField('Last Name', validators=[DataRequired(), Length(
        min=3, max=25)], render_kw={"placeholder": "enter your last name", 'id': 'inputEmail4'})

    username = StringField('user name', render_kw={
                           "placeholder": "username", 'id': 'inputEmail4'})

    email = EmailField('Email Addres', validators=[DataRequired(), Email()], render_kw={
                       "placeholder": "your email address: name@example.com", 'id': 'inputEmail4'})

    phone_number = StringField(
        'Number', render_kw={"placeholder": "your phone number", 'id': 'inputEmail4'})

    password = PasswordField('password', validators=[DataRequired(), Length(
        min=8)],  render_kw={"placeholder": "enter your password", 'id': 'inputPassword4'})

    confirm_password = PasswordField(' password', validators=[DataRequired(), EqualTo(
        'password')],  render_kw={"placeholder": "confirm your password", 'id': 'inputPassword4'})

    submit = SubmitField(
        render_kw={"value": "REGISTER", 'class': 'btn btn-primary'})
