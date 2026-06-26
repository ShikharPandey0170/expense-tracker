def expense(expenses, month):
    matching = []
    
    for e in expenses:
        if e['date'].split('/')[1] == month:
            matching.append(e)
    
    total = 0.0
    
    for e in matching:
        total += e['amount']
    
    return total, matching