from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import NumberRange, DataRequired

class BookForm(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[NumberRange(min=1, max=10)])
    submit = SubmitField("Add Book")
