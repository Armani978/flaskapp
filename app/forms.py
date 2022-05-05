from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    pokemon = StringField('pokemon', validators=[DataRequired()])
    submit = SubmitField('Submit')
    