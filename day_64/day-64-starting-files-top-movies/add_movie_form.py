from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[InputRequired()])
    submit = SubmitField("Add Movie")