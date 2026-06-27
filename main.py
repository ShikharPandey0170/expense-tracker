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
            while True:
                category_choice = input("Select Category:\n1. Food\n2. Bills\n3. Transportation\n4. Health\n5. Education\n6. Miscellaneous\n:- ")
                category = category_map.get(category_choice)
                if category:
                    break
                print("Invalid category choice! Please enter 1-6.")

            while True:
                try:
                    amount = float(input("Enter Amount:- Rs. "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    break
                except ValueError:
                    print("Invalid amount! Please enter a number.")

            while True:
                date = input("Enter Date (DD/MM/YYYY):- ")
                parts = date.split('/')
                if len(parts) == 3 and len(parts[0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4:
                    break
                print("Invalid date format! Please use DD/MM/YYYY.")

            add.expense(expenses, category, amount, date)

        elif ch == 2:
            while True:
                month = input("Enter month to view (MM):- ")
                if month.isdigit() and 1 <= int(month) <= 12:
                    break
                print("Invalid month! Please enter a number between 01 and 12.")
            view.expenses(expenses, month)

        elif ch == 3:
            while True:
                month = input("Enter month to calculate total (MM):- ")
                if month.isdigit() and 1 <= int(month) <= 12:
                    break
                print("Invalid month! Please enter a number between 01 and 12.")
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
            while True:
                try:
                    budget = float(input("Enter new monthly budget:- Rs. "))
                    if budget < 0:
                        print("Budget cannot be negative!")
                        continue
                    break
                except ValueError:
                    print("Invalid budget! Please enter a number.")
            save.budget(budget)
            print("Budget Updated!")

        elif ch == 5:
            while True:
                target = input("Enter date to delete (DD/MM/YYYY):- ")
                parts = target.split('/')
                if len(parts) == 3 and len(parts[0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4:
                    break
                print("Invalid date format! Please use DD/MM/YYYY.")
            count = delete.expense(expenses, target)
            
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