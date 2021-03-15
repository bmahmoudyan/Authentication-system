from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()],  render_kw={
                           "placeholder": "email username phone number"})
    password = PasswordField(' password', validators=[DataRequired()],  render_kw={
                             "placeholder": "password"})

    submit = SubmitField(render_kw={"value": "GO"})
