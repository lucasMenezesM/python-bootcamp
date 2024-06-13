from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired(), validators.Length(min=8, message="There should be at least 6 characters")])
    submit = SubmitField(label="Submit", validators=[DataRequired()])