from wtforms import Form, StringField, validators
from flask import Flask
import pandas as pd


app = Flask(__name__)

with app.open_resource('static/drop_down.csv') as p:
    drop_down = pd.read_csv(p) 

positions = []

class InputForm(Form):
    A = SelectField(
        label='Start Position', default='Computer Operations Specialist 1')
    B = SelectField(
        label='End Position', default='Tech Title 3')
