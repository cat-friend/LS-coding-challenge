from app.models import db, Loan


# Adds a demo user, you can add other users here if you want
def seed_loans():
    amounts = [2000, 4000, 40000, 10000, 90000, 2500, 1800000]
    interest_rates = [1.3, 2.25, 7.3, 13.45, 10.354, 23.123, 0.123]
    lengths_months = [10.5, 28.3, 31, 14.5, 5.9, 16, 27]
    monthly_payments = [10, 200, 3000, 4400, 50, 665, 7000]
    for i in range(0, 7):
        loan = Loan(amount=amounts[i], interest_rate=interest_rates[i], length_months=lengths_months[i], monthly_payment=monthly_payments[i])
        db.session.add(loan)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_loans():
    db.session.execute('TRUNCATE loans RESTART IDENTITY CASCADE;')
    db.session.commit()
