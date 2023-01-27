from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField, BooleanField, SubmitField, HiddenField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import Profile, User

class ProfileForm(FlaskForm):
    membertype = SelectField('Member Type', validators=[DataRequired()], choices=[('CST','Certified Scrum Trainer'),('CSP', 'Certified Scrum Practioner')])
    apply = SubmitField('Apply')

class UserForm(FlaskForm):
    usertype = SelectField('User Type', validators=[DataRequired()], choices=[('CUS','Customer'),('ADM', 'Admin')])
    save = SubmitField('Save')

class EditForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    member_type = SelectField('Member Type', validators=[DataRequired()], choices=[('CST','Certified Scrum Trainer'),('CSP', 'Certified Scrum Practioner')])
    rating = StringField('Rating', validators=[DataRequired()])
    save = SubmitField('Save')

class ExpForm(FlaskForm):
    exp_qual = StringField('Experience/Qualification', validators=[DataRequired()])
    save = SubmitField('Save')
    
