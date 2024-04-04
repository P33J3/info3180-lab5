# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired('Required'), DataRequired('Please enter Title')])
    description = TextAreaField('Description', validators=[InputRequired('Required'), DataRequired('Please enter Description')])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'],
    'Images only')])
