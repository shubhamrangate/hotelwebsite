from flask import Flask, render_template,url_for,flash,redirect,request
#from hotelwebsite.forms import RegistrationForm,LoginForm,ReservetableForm
#from hotelwebsite.models import User,Login,Reserve
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='a7d978146a2d7f855c59294fecf4a994'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login'

from hotelwebsite import routes  
#class User(db.Model):
#	id=db.Column(db.Integer,primary_key=True)
#	username=db.Column(db.String(20),unique=True,nullable=False)
#	email=db.Column(db.String(30),unique=True,nullable=False)
#	password=db.Column(db.String(60),nullable=False)
#
#	def __repr__(self):
#		return f"User('{ self.username }','{ self.email }')"

#class Login(db.Model):
#	id=db.Column(db.Integer,primary_key=True)
#	email=db.Column( db.String(20),db.ForeignKey('user.email'),unique=True,nullable=False)
#	password=db.Column( db.String(60),db.ForeignKey('user.password'),nullable=False)

#	def __repr__(self):
#		return f"Login('{self.email}')"



#class Reserve(db.Model):
#	id=db.Column(db.Integer,primary_key=True)
#	guest=db.Column(db.Integer,nullable=False)
#	section=db.Column(db.String(20),default="nonsmoking")
#	date=db.Column(db.DateTime)
#	time=db.Column(db.String(20))
#	def __repr__(self):
#		return f"Reserve('{self.guest}','{self.section}','{self.date}','{self.time}')"


