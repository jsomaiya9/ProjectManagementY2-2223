from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import News

class NewsForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    caption = TextAreaField('Caption', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    save = SubmitField('Save')