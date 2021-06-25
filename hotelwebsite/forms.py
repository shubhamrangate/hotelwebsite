from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField,TextAreaField
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,Optional
from hotelwebsite.models import User
import phonenumbers



class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	Confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. please choose a different.')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. please choose a different.')


class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Log In')

class ReservetableForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	guest=RadioField('Number Of Guest', choices = [('one','1'),('two','2'),('three','3'),('four','4'),('five','5'),('six','6')])
	section=RadioField('Section',choices=[('nonsmoking','Non-smoking'),('smoking','Smoking')])
	date = DateField('Date', format='%Y-%m-%d')
	time = TimeField('Time')
	submit=SubmitField('Reserve')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class FeedBackForm(FlaskForm):
	username=StringField('User',validators=[DataRequired(),Length(min=2, max=20)])
	mobno=StringField("(+country code)Mob-No",validators=[DataRequired()])
	email=StringField('Email',validators=[DataRequired(),Email()])
	comment=TextAreaField('Your Feedback',validators=[Optional(),Length(min=0,max=100)])
	submit=SubmitField('Send Feedback')

	def validate_phone(self,phone):
		p=phonenumbers.parse(mobno.data)
		if not phonenumbers.is_valid_number(p):
			raise ValidationError('Invalid Phone number')


class MenuForm(FlaskForm):
	utthapizza=RadioField('Do you Serve utthapizza',choices=[('menu1','yes'),('nomenu1','no')])
	dosa=RadioField('Do you Serve Dosa',choices=[('menu2','yes'),('nomenu2','no')])
	idali=RadioField('Do you Serve idali',choices=[('menu3','yes'),('nomenu3','no')])
	cofee=RadioField('Do you Serve cofee',choices=[('menu4','yes'),('nomenu4','no')])
	uditvada=RadioField('Do you Serve uditvada',choices=[('menu5','yes'),('nomenu5','no')])
	submit=SubmitField('Place the Orders')
