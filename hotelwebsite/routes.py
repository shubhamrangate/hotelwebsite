from flask import render_template,url_for,flash,redirect,request
from hotelwebsite.hotel_website import app,db,bcrypt
from hotelwebsite.forms import RegistrationForm,LoginForm,ReservetableForm,UpdateAccountForm,FeedBackForm,MenuForm
from hotelwebsite.models import User,Login,Reserve,Feedback,Menulist
from flask_login import login_user,current_user, logout_user, login_required
#from flask_sqlalchemy  import SQLAlchemy
#from flask_bcrypt import Bcrypt


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')


db.create_all()


@app.route("/contact",methods=['GET','POST'])

def contact():
	form=FeedBackForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user:
			feedback1=Feedback(username=form.username.data,mobno=form.mobno.data,email=form.email.data,comment=form.comment.data)
			db.session.add(feedback1)
			db.session.commit()
			feedback2=Feedback().query.first()
			if feedback2:
				flash('your feedback is successfully submited','success')
				return redirect(url_for('contact'))
			else:
				return redirect(url_for('contact'))
		else:
			flash('Please enter the valid username and email','danger')
	return render_template('contact.html',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for! you are now able to login','success')
		return redirect(url_for('login'))
	return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful.Please check username and password','danger')
	return render_template('login.html',form=form)


@app.route('/reservetable',methods=['GET','POST'])
@login_required
def reservetable():
	form=ReservetableForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user:
			current_user.email=form.email.data
			current_user.guest=form.guest.data
			current_user.section=form.section.data
			current_user.date=form.date.data
			current_user.time=form.time.data
			date1=form.date.data.strftime("%d:%m:%Y")
			time1=form.time.data.strftime("%H:%M")
			reserve=Reserve(email=form.email.data,guest=form.guest.data,section=form.section.data,date=date1,time=time1)
			db.session.add(reserve)
			db.session.commit()
			reserve1=Reserve.query.first()
			if reserve1:
				flash('you have successfully reserve the tables','success')
			else:
			    return redirect(url_for('reservetable'))
		else:
			flash('Please enter the valid email','danger')
	return render_template('reservetable.html',form=form)


@app.route('/menu',methods=['GET','POST'])
def menu():
	form=MenuForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=current_user.email).first()
		if user:
			menulist1=Menulist(email=current_user.email,utthapizza=form.utthapizza.data,dosa=form.dosa.data,idali=form.idali.data,cofee=form.cofee.data,uditvada=form.uditvada.data)
			db.session.add(menulist1)
			db.session.commit()
			menulist2=Menulist.query.first()
			if menulist2:
				flash('your dishes will be ready.Please Reserve the table','success')
				return redirect(url_for('reservetable'))
			else:
				flash('sorry for you','danger')
				return redirect(url_for('menu'))
		else:
			flash('you are not the valid user')
	return render_template('menu.html',form=form)
	



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
	form=UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username=form.username.data
		current_user.email=form.email.data
		db.session.commit()
		flash('your account has been updated!','success')
		return redirect(url_for('account'))
	elif request.method=='GET':
		form.username.data=current_user.username
		form.email.data=current_user.email
	return render_template('account.html',form=form)
