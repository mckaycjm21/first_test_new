from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
db = SQLAlchemy(app)


class Pet(db.Model):
        __tablename__ = 'pets'

        

        def __repr__(self):
            p = self
            return f"<Pet id = {p.id} name = {p.name} species = {p.species} hunger = {p.hunger}>"

        id = db.Column(db.Integer,
                       primary_key = True,
                       autoincrement = True)
        
        name = db.Column(db.String(50),
                         nullable = False,
                         unique = True)
        
        species = db.Column(db.String(30),
                            nullable = True)
        
        hunger = db.Column(db.Integer,
                           nullable = True,
                           default = 20)
        