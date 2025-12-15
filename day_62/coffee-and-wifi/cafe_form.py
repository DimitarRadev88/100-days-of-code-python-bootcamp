from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe name", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps(URL)", validators=[DataRequired(), URL()])
    opening_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating",
                                choices=[("", ""), ("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕"),
                                         ("☕☕☕☕☕", "☕☕☕☕☕")], validators=[DataRequired()])
    wifi_rating = SelectField(label="Wifi Strength Rating",
                              choices=[("", ""), ("✘", "✘"), ("✘✘", "✘✘"), ("✘✘✘", "✘✘✘"), ("✘✘✘✘", "✘✘✘✘"),
                                       ("✘✘✘✘✘", "✘✘✘✘✘")], validators=[DataRequired()])
    power_sockets = SelectField(label="Power Socket Availability",
                                choices=[("", ""), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"),
                                         ("🔌🔌🔌🔌", "🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField(label="Submit")
