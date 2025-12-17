from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[InputRequired(), NumberRange(min=1, max=10)])
    review = StringField("Your Review", validators=[InputRequired()])
    submit = SubmitField("Done")
