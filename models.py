from wtforms import Form, StringField, validators

class InputForm(Form):
    A = StringField(
        label='Start Position', default='Computer Operations Specialist 1',
        validators=[validators.InputRequired()])
    B = StringField(
        label='End Position', default='Tech Title 3',
        validators=[validators.InputRequired()])
