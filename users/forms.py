from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    login_method = StringField('username', validators=[DataRequired()],  render_kw={
                               "placeholder": "email username or phone number", 'id': 'inputEmail4', "class": 'form-control'})
    password = PasswordField(' password', validators=[DataRequired()],  render_kw={
                             "placeholder": "password", 'class': "form-control", 'id': 'inputPassword4'})
    submit = SubmitField(render_kw={"value": "LOGIN", 'class': 'btn btn-primary'})


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=25)])
    username = StringField('Email Address')
    email = EmailField('Email Addres', validators=[DataRequired()])
    phone_number = StringField('Number')
    password = PasswordField(' password', validators=[DataRequired()],  render_kw={"placeholder": "password", 'class': "form-control", 'id': 'inputPassword4'})
    confirm_password = PasswordField(' password', validators=[DataRequired()],  render_kw={"placeholder": "password", 'class': "form-control", 'id': 'inputPassword4'})
