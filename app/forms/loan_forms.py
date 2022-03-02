from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def greater_than_zero(form, field):
    data = field.data
    if not data > 0:
        raise ValidationError(f"{field} value must be greater than 0.")

def less_than_one_hundred(form, field):
    data = field.data
    if data > 100:
        raise ValidationError(f"{field} value cannot be greater than 100.")

class LoanForm(FlaskForm):
    amount = DecimalField("", validators=[DataRequired(), greater_than_zero])
    interest_rate = DecimalField("", validators=[DataRequired(), greater_than_zero, less_than_one_hundred])
    length_months = DecimalField("", validators=[DataRequired(), greater_than_zero, NumberRange(max=999, message="Length in months cannot be greater than 999.")])
    monthly_payment = DecimalField("", validators=[DataRequired(), greater_than_zero])