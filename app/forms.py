from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import NumberRange, optional

validators = [optional()]

class ComputeForm(FlaskForm):
    t1 = DecimalField('Test 1', validators=validators)
    t2 = DecimalField('Test 2', validators=validators)
    t3 = DecimalField('Test 3', validators=validators)
    t4 = DecimalField('Test 4', validators=validators)
    t5 = DecimalField('Test 5', validators=validators)
    fl = DecimalField('Final', validators=validators)
    hw = DecimalField('Homework', validators=validators)
    submit = SubmitField('Calculate')