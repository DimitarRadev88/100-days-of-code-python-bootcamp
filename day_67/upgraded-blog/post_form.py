from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    author = StringField("Your Name", validators=[InputRequired()])
    img_url = StringField("Blog Image Url", validators=[InputRequired()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("SUBMIT POST")