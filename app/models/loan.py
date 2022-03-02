from .db import db
from sqlalchemy.sql import func

class Loan(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Decimal(12,2), min=0, nullable=False)
    interest_rate = db.Column(db.Decimal(7,5), min=0, max=100, nullable=False)
    length_months = db.Column(db.Decimal(5,2), min=0, nullable=False)
    monthly_payment = db.Column(db.Decimal(10,2), min=0, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

def to_dict(self):
    return {
        'id': self.id,
        'amount': self.amount,
        'interest_rate': self.interest_rate,
        'length_months': self.length_months,
        'monthly_payment': self.monthly_payment,
        'created_at': self.created_at,
        'updated_at': self.updated_at
    }
