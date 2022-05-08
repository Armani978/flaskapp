from flask import render_template, request
import requests
from flask_wtf import FlaskForm
from app import app
from .forms import PokeForm , Login, Register


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/poke', methods=['GET','POST'])
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
    return render_template('poke.html.j2', form=form)
@app.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    return render_template('login.html.j2', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    return render_template('register.html.j2', form=form)
