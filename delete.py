def expense(expenses, date):
    length = len(expenses)
    new_expenses = []
    for e in expenses:
        if e['date'] != date:
            new_expenses.append(e)
    expenses[:] = new_expenses
    return length - len(expenses)