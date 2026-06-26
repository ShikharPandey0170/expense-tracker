def expense(expenses, category, amount, date):
    expenses.append({'category': category, 'amount': amount, 'date': date})
    print("Expense added successfully!")