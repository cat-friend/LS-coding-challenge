from .db import db
from sqlalchemy.sql import func

class Loan(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(12,2), nullable=False)
    interest_rate = db.Column(db.Numeric(7,5), nullable=False)
    length_months = db.Column(db.Integer, nullable=False)
    monthly_payment = db.Column(db.Numeric(10,2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'amount': f"{self.amount}",
            'interest_rate': f"{self.interest_rate}",
            'length_months': f"{self.length_months}",
            'monthly_payment': f"{self.monthly_payment}",
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
