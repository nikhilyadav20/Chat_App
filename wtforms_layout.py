from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    # Registration Form

    username = StringField('username', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), Length(min=4, max=25, message="Password must be between 4 and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd', validators=[InputRequired(message="Password required"), EqualTo('password', message="Passwords must match")])

    submit_button = SubmitField('Create')