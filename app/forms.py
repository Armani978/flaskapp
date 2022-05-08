from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    pokemon = StringField('pokemon', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Login(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Register(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
