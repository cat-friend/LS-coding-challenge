from re import L
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import DecimalField, IntegerField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from app.models import Loan


def greater_than_zero(form, field):
    data = field.data
    if not data > 0:
        raise ValidationError(f"{field} value must be greater than 0.")

def less_than_one_hundred(form, field):
    data = field.data
    if data > 100:
        raise ValidationError(f"{field} value cannot be greater than 100.")

def less_than_amount(form, field):
    amount = form.data['amount']
    length_months = form.data['length_months']
    monthly_payment = field.data
    if monthly_payment >= amount and length_months > 1:
        raise ValidationError(f"{field} must be less than total amount when the number of months left in repayment is greater than 1.")

class LoanForm(FlaskForm):
    amount = DecimalField("", validators=[DataRequired(), greater_than_zero])
    interest_rate = DecimalField("", validators=[DataRequired(), greater_than_zero, less_than_one_hundred])
    length_months = IntegerField("", validators=[DataRequired(), greater_than_zero, NumberRange(max=999, message="Length in months cannot be greater than 999.")])
    monthly_payment = DecimalField("", validators=[DataRequired(), greater_than_zero, less_than_amount])

class EditLoanForm(FlaskForm):
    id = IntegerField("", validators=[DataRequired(), greater_than_zero])
    amount = DecimalField("", validators=[DataRequired(), greater_than_zero])
    interest_rate = DecimalField("", validators=[DataRequired(), greater_than_zero, less_than_one_hundred])
    length_months = IntegerField("", validators=[DataRequired(), greater_than_zero, NumberRange(max=999, message="Length in months cannot be greater than 999.")])
    monthly_payment = DecimalField("", validators=[DataRequired(), greater_than_zero, less_than_amount])
