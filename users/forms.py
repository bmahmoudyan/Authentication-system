from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login_method = StringField('username', validators=[DataRequired()],  render_kw={
                               "placeholder": "email username or phone number", 'id': 'inputEmail4', "class": 'form-control'})
    password = PasswordField(' password', validators=[DataRequired()],  render_kw={
                             "placeholder": "password", 'class': "form-control", 'id': 'inputPassword4'})
    submit = SubmitField(render_kw={"value": "LOGIN", 'class': 'btn btn-primary'})
