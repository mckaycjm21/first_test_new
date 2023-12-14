from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddSnackForm(FlaskForm):
    """Form for adding snacks"""


    price = FloatField("Price in USD")
    name = StringField("Snack Name")


class NewEmployeeForm(FlaskForm):

    name = StringField("Employee Name")
    state = StringField("State")
    dept_code = StringField("Department Code")