import csv

def budget(budget):
    with open('budget.txt', 'w') as f:
        f.write(str(budget))

def expenses(expenses):
    if not expenses:
        try:
            open('expenses.csv', 'w').close()
        except:
            pass
        return
    
    fieldnames = ['category', 'amount', 'date']
    
    with open('expenses.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)