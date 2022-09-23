from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class CreatePetForm(FlaskForm):
    """Form for adding pet to database"""

    accepted_species = ['dog', 'cat', 'porcupine']

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(values=accepted_species, message="Must be a dog, cat, or porcupine.")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL("Photo must be a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=1, max=30, message="Age must be between 1 and 30.")])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", default=True)