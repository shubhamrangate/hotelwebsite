from datetime import datetime
from hotelwebsite.hotel_website import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
    

class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(30),unique=True,nullable=False)
	password=db.Column(db.String(60),nullable=False)

	def __repr__(self):
		return f"User('{ self.username }','{ self.email }')"

class Login(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column( db.String(20),db.ForeignKey('user.email'),unique=True,nullable=False)
	password=db.Column( db.String(60),db.ForeignKey('user.password'),nullable=False)

	def __repr__(self):
		return f"Login('{self.email}')"



class Reserve(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column( db.String(20),db.ForeignKey('user.email'),nullable=False)
	guest=db.Column(db.Integer,nullable=False)
	section=db.Column(db.String(20),default="nonsmoking")
	date=db.Column(db.String(40))
	time=db.Column(db.String(20))
	def __repr__(self):
		return f"Reserve('{self.guest}','{self.section}','{self.date}','{self.time}')"


class Feedback(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),db.ForeignKey('user.username'),nullable=False)
	mobno=db.Column(db.String(15))
	email=db.Column(db.String(20),db.ForeignKey('user.email'),nullable=False)
	comment=db.Column(db.String(100))
	def __repr__(self):
		return f"Feedback('{self.username}','{self.mobno}','{self.email}','{self.comment}')"


class Menulist(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(20),db.ForeignKey('user.username'),nullable=False)
	utthapizza=db.Column(db.String(5),default='nomenu1')
	dosa=db.Column(db.String(5),default='nomenu2')
	idali=db.Column(db.String(5),default='nomenu3')
	cofee=db.Column(db.String(5),default='nomenu4')
	uditvada=db.Column(db.String(5),default='nomenu5')
	def __repr__(self):
		return f"Menulist('{self.email}','{self.utthapizza}','{self.dosa}','{self.idali}','{self.cofee}','{self.uditvada}')"