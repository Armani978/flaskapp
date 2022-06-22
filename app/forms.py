from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError, email_validator
from .models import User

class PokeForm(FlaskForm):
    pokemon = StringField(' ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CatchPokemon(FlaskForm):
    pokemon = StringField(' ', validators=[DataRequired()])
    submit=SubmitField('Add pokemon')

class Login(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')

class Register(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')
    
    def validate_email(form, field):
        same_user_email = User.query.filter_by(email = field.data).first()
        if same_user_email:
            raise ValidationError('Sorry, the email is in use. Pick another one.')

class EditProfile(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')
