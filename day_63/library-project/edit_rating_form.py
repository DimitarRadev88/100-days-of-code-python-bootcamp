from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import NumberRange, DataRequired

class EditRatingForm(FlaskForm):
    rating = FloatField("", render_kw={"placeholder": "New Rating"}, validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField("Change Rating")
