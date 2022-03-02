from flask import Blueprint, request
from app.models import Loan, db
from app.forms import LoanForm

loan_routes = Blueprint('loans', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list.
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'"{field}: {error}')
    return errorMessages


@loan_routes.route('/', methods=['POST', 'GET'])
def all_loans():
    """
    POST requests - posts new loans with payload from frontend. If successful,
    the route returns JSON data needed for the frontend. Else, the route
    returns error messages.
    GET requests - returns JSON data for all loans.
    """
    if request.method == 'GET':
        loans = Loan.query.all()
        return {"loans": [loan.to_dict() for loan in loans]}
    if request.method == 'POST':
        form = LoanForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            amount = form.data['amount']
            interest_rate = form.data['interest_rate']
            length_months = form.data['length_months']
            monthly_payment = form.data['monthly_payment']
            new_loan = Loan(amount=amount, interest_rate=interest_rate, length_months=length_months, monthly_payment=monthly_payment)
            db.add(new_loan)
            db.commit()
            return new_loan.to_dict()
        else:
            return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@loan_routes.route('/<int:id>', methods=['GET', 'PUT'])
def one_loan(id):
    """
    PUT requests - updates existing loans with payload from frontend. If successful,
    the route returns JSON data needed for the frontend. Else, the route
    returns error messages.
    GET requests - returns JSON data for specific loan.
    """
    if request.method == 'GET':
        try:
            loan = Loan.query.filter_by(id=id).all()
            return loan.to_dict()
        except:
            return {'errors': "resource not found"}, 404
    if request.method == 'PUT':
        loan = Loan.query.filter_by(id=id).all()
        if not loan:
            return {'errors': "resource not found"}, 404
        else:
            form = LoanForm()
            form['csrf_token'].data = request.cookies['csrf_token']
            if form.validate_on_submit():
                loan.amount = form.data['amount']
                loan.interest_rate = form.data['interest_rate']
                loan.length_months = form.data['length_months']
                loan.monthly_payment = form.data['monthly_payment']
                db.add(loan)
                db.commit()
                return loan.to_dict()
            else:
                return {'errors': validation_errors_to_error_messages(form.errors)}, 401
