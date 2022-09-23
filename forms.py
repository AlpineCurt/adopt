from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional

class CreatePetForm(FlaskForm):
    """Form for adding pet to database"""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])