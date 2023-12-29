from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake, create_all_db

import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "donttellanyone123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template('index.html')

@app.route('/api/cupcakes')
def get_all_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)

@app.route('/api/cupcakes/<id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id).serialize()
    return jsonify(cupcake)

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    image = request.json.get('image', None)
    if image:
        new_cupcake = Cupcake(flavor = request.json['flavor'],
                                            size = request.json['size'], 
                                            rating = request.json['rating'],
                                            image = request.json['image'])
        
    else:
        new_cupcake = Cupcake(flavor = request.json['flavor'],
                                            size = request.json['size'], 
                                            rating = request.json['rating'])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake = new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<id>', methods = ['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()))

@app.route('/api/cupcakes/<id>', methods = ['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = "deleted")
    