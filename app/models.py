from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    pokemen=db.relationship('Data',
                    secondary='users_pokemon',
                    backref='users',
                    lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'

    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'

    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hash(self,login_password):
        return check_password_hash(self.password, login_password)

    def my_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])

    def save(self):
        db.session.add(self)
        db.session.commit()

    def catch(self, pokemon):
        self.pokemen.append(pokemon)
        db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Data(db.Model):
    pokemon_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    hp = db.Column(db.Integer)
    ability = db.Column(db.String)
    base_experience = db.Column(db.Integer)
    front_shiny= db.Column(db.String)
    attack_base_stat=db.Column(db.Integer)
    defense_base_stat = db.Column(db.Integer)
    
    def __str__(self):
        return f'{self.pokemon_id | self.name }'
    

    def poke_dict(self, pokemon):
        self.name = pokemon['name']
        self.hp = pokemon['hp']
        self.ability = pokemon['ability']
        self.base_experience = pokemon['base_experience']
        self.attack_base_stat = pokemon['attack_base_stat']
        self.defense_base_stat = pokemon['defense_base_stat']
        self.front_shiny = pokemon['front_shiny']
    def save(self):
        db.session.add(self)
        db.session.commit()

    def catch(self, pokemon):
        self.pokemen.append(pokemon)
        db.session.commit()

class UsersPokemon(db.Model):
    pokemon_id = db.Column(db.Integer, db.ForeignKey('data.pokemon_id'),primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)

    def __repr__(self):
        return f'<UsersPokemon: {self.pokemon_id} | {self.id}>'
