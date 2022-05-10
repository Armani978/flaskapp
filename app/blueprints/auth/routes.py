import requests
from flask import render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from .import bp as auth
from ...forms import EditProfile, PokeForm
from ...models import User
from flask_login import current_user, logout_user, login_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


    


@auth.route("/index", methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@auth.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfile()
    if request.method == 'POST' and form.validate_on_submit():
        user_dict={
                "first_name" : form.first_name.data.title(),
                "last_name" : form.last_name.data.title(),
                "email": form.email.data.lower(), 
                "password": form.password.data
            }
        user = User.query.filter_by(email=user_dict["email"]).first()
        if user and user.email != current_user.email:
            flash('Email in use. Pick another email address')
            return redirect(url_for('auth.edit_profile'))
        try:
            current_user.my_dict(user_dict) 
            current_user.save()
            flash("Profile changed.")   
        except:
            flash('Error. Please Try again', 'danger')
            return redirect(url_for('auth.edit_profile'))
        return redirect(url_for('auth.index'))
    return render_template('register.html.j2', form=form)

@auth.route('/poke', methods=['GET','POST'])
@login_required
def poke():
    form = PokeForm()
    if request.method == 'POST':
        pokemon = form.pokemon.data.lower()
        
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.ok:
            
            stat = response.json()
            poke_stats = []
            # for stat in poke_stats:
            stats = {}
            stats = {
                "name" : stat['name'],
                "ability":stat['abilities'][0]['ability']['name'],
                "base_experience":stat['base_experience'],
                "front_shiny":stat['sprites']['front_shiny'],
                "attack_base_stat":stat['stats'][1]['base_stat'],
                "hp_base_stat":stat['stats'][0]['base_stat'],
                "defense_base_stat":stat['stats'][2]['base_stat']
            }
            poke_stats.append(stats)
            return render_template('poke.html.j2',pokes=poke_stats,form=form)
    return render_template('poke.html.j2',form=form)       
@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        return redirect(url_for('main.login'))
