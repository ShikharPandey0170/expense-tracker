def expenses(expenses, month):
    matching = []
    for e in expenses:
        if e['date'].split('/')[1] == month:
            matching.append(e)
    if not matching:
        print("No expenses found for this month.")
        return
    print("\nID \t Amount (Rs.) \t Date \t Category")
    for i, e in enumerate(matching, 1):
        print(f"{i} \t Rs. {e['amount']:.2f} \t {e['date']} \t {e['category']}")
