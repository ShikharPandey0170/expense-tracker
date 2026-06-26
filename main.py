import add, delete, load, save, total, view

budget = load.budget()
expenses = load.expenses()

while True:
    print("\n\tPERSONAL EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Change Monthly Budget")
    print("5. Delete an Expense")
    print("6. Save & Exit")

    try:
        ch = int(input("\nEnter your choice:- "))
        if ch == 1:
            category_map = {'1': 'Food', '2': 'Bills', '3': 'Transportation', '4': 'Health', '5': 'Education', '6': 'Miscellaneous'}
            category_choice = input("Select Category:\n1. Food\n2. Bills\n3. Transportation\n4. Health\n5. Education\n6. Miscellaneous\n:- ")
            category = category_map.get(category_choice, 'Miscellaneous')
            
            amount = float(input("Enter Amount:- Rs. "))
            date = input("Enter Date (DD/MM/YYYY):- ")
            
            add.expense(expenses, category, amount, date)

        elif ch == 2:
            month = input("Enter month to view (MM):- ")
            view.expenses(expenses, month)
        
        elif ch == 3:
            month = input("Enter month to calculate total (MM):- ")
            tot, matching = total.expense(expenses, month)
            
            if tot > 0:
                print(f"\n\tTOTAL EXPENSE FOR MONTH {month}\n")
                print(f"Total Expense:- Rs. {tot:.2f}")
                
                if tot > budget:
                    print(f"Warning:- You exceeded your budget by Rs. {(tot - budget):.2f}!")
                else:
                    print(f"Remaining Budget:- Rs. {(budget - tot):.2f}")
            else:
                print("No expenses found for this month.")
        
        elif ch == 4:
            budget = float(input("Enter new monthly budget:- Rs. "))
            save.budget(budget)
            print("Budget Updated!")
        
        elif ch == 5:
            target = input("Enter date to delete (DD/MM/YYYY):- ")
            count = delete.expenses(expenses, target)
            
            print(f"Deleted {count} expense(s) for date {target}")
            if count > 0:
                save.expenses(expenses)
        
        elif ch == 6:
            save.expenses(expenses)
            save.budget(budget)
            print("\nAll data saved!")
            break

        else:
            raise(ValueError)
    except ValueError:
        print("Invalid choice! Try again.")
        continue