from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired(), validators.Length(max=300, message="There should be at maximum 300 characters and it's required.")])
    year = StringField(label='Year', validators=[DataRequired(), validators.Length(max=4, message="There should be at maximum 4 digits and it's required.")])
    rating = StringField(label='Rating', validators=[DataRequired()])
    raking = StringField(label='Raking', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired(), validators.Length(max=300, message="There should be at maximum 300 characters and it's required.")])
    img_url = StringField(label='Rating', validators=[DataRequired()])
    submit = SubmitField(label="Update", validators=[DataRequired()])


class UpdateForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired(), validators.Length(max=300, message="There should be at maximum 300 characters and it's required.")])
    submit = SubmitField(label="Update", validators=[DataRequired()])


class AddMovieForm(FlaskForm):
    title = StringField(label="Type the movie's name", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie", validators=[DataRequired()])
