from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, URL, Length

class PetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message = "Name can not be blank")])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[InputRequired(), URL()])
    age = FloatField("Age")
    notes = StringField("Notes")
    available = BooleanField("Available")
