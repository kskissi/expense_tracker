from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Expense('{self.description}', '{self.amount}', '{self.date}')"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        new_expense = Expense(description=description, amount=amount)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))

    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total_expenses = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081) # Modified to use host='0.0.0.0'
