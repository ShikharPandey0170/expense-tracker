import csv

def budget():
    budget = 0.0
    try:
        with open('budget.txt', 'r') as f:
            budget = float(f.read().strip())
        print(f"Loaded previous budget:- Rs. {budget:.2f}")
    
    except FileNotFoundError:
        budget = float(input("Enter your monthly budget:- Rs. "))
        print(f"Starting with new budget:- Rs. {budget:.2f}")
    
    except Exception as e:
        print(f"Error reading budget file:- {e}")
        budget = float(input("Enter your monthly budget:- Rs. "))
        print(f"Starting with new budget:- Rs. {budget:.2f}")
    
    return budget

def expenses():
    expenses = []
    try:
        with open('expenses.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print(f"Loaded {len(expenses)} previous expenses.")
    
    except FileNotFoundError:
        pass
    
    except Exception as e:
        print(f"Warning:- Could not load expenses.\nError:- ({e})")
    
    return expenses