from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, URL

class NewPostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Author's name", validators=[DataRequired()])
    img_url = StringField(label="Background img url", validators=[DataRequired()])
    textarea = CKEditorField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Send")