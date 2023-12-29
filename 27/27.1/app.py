from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, create_all
from forms import PetForm
import requests
from secret import youtube_api_key


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "donttellanyone123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_homepage():
    resp = requests.get(
                        "https://itunes.apple.com/search",
                        params={"term": "Aaliyah", "limit": 10}
                        )
    pets = Pet.query.all()
    return render_template('index.html', pets = pets, resp = resp, youtube_key = youtube_api_key)

@app.route('/pet/add', methods = ['GET', 'POST'])
def create_new_pet():
    form = PetForm()
    name = form.name.data
    species = form.species.data
    photo = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data

    if form.validate_on_submit():
        pet = Pet(name = name, species = species, photo_url = photo, age = age, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()
        flash('You have just created a new pet entry!')
        return redirect(f'/pet/{pet.id}')

    else:
        return render_template('add_pet.html', form = form)

@app.route('/pet/<int:id>/edit', methods = ['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        flash('You have just edit your pet entry!')
        return redirect(f'/pet/{pet.id}')

    else:
        return render_template('edit_pet.html', form = form, pet = pet)

@app.route('/pet/<int:id>')
def show_pet(id):
    pet = Pet.query.get_or_404(id)
    return render_template('show_pet.html', pet = pet)

@app.route('/pet/confirmation/')
def confirm_add_snack():
    return render_template('confirmation.html')

