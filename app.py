from crypt import methods
from operator import methodcaller
from flask import Flask, request, render_template, redirect, flash, session, get_flashed_messages
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import CreatePetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "fluffyhuskytails"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """display homepage"""
    pets = Pet.query.limit(5)
    return render_template('home.html', pets=pets)

@app.route("/add", methods=['GET', 'POST'])
def add_pet():
    """Form for adding a pet to database"""
    form = CreatePetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    """Show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = CreatePetForm(obj=pet)
    #raise
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("show_pet.html", form=form, pet=pet)