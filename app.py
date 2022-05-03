from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/poke', methods=['GET','POST'])
def poke():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
           
        
        poke_stats = []
        for stat in poke_stats:
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
            return render_template('poke.html.j2', pokemon=poke_stats)
        
    return render_template('poke.html.j2')