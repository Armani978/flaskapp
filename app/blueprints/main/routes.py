from flask import render_template, request, flash, redirect, url_for
import requests
from .import bp as main
from ...forms import Login, Register, EditProfile
from ...models import User
from flask_login import current_user, logout_user, login_user, login_required


@main.route('/', methods=['GET','POST'])
def login():
    form = Login()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        user_query=User.query.filter_by(email=email).first()
        if user_query and user_query.check_hash(password):
            login_user(user_query)
            flash('Welcome','success')
            return redirect(url_for('auth.index'))
        return render_template('login.html.j2', form=form)
    return render_template('login.html.j2', form=form)

@main.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            user_dict={
                "first_name" : form.first_name.data.title(),
                "last_name" : form.last_name.data.title(),
                "email": form.email.data.lower(), 
                "password": form.password.data
            }     
            user_object = User()
            user_object.my_dict(user_dict)
            user_object.save()


        
        except:
            flash("Error, try again.", "danger")
            return render_template('register.html.j2', form=form)
        flash("Success! You have registered!")    
        return redirect(url_for('main.login'))
    return render_template('register.html.j2', form=form)

