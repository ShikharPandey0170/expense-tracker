# Personal Expense Tracker

A Python CLI application to manage personal expenses, track monthly budgets, and save expense data using file handling.

## Features

- **Add Expenses** - Record expenses with category, amount, and date
- **View Expenses** - Filter and view expenses by month
- **Calculate Total** - View total expenses for a month with budget comparison
- **Change Budget** - Update your monthly budget anytime
- **Delete Expenses** - Remove expenses by date
- **Persistent Storage** - Data saved to files (CSV and TXT) for persistence

## Available Categories

1. Food
2. Bills
3. Transportation
4. Health
5. Education
6. Miscellaneous

## Installation & Usage

1. Ensure you have Python installed
2. Clone or download the project files
3. Run the main program:

```bash
python main.py
```

## How It Works

- **Budget** is stored in `budget.txt` - Your monthly budget limit
- **Expenses** are stored in `expenses.csv` - All recorded expenses with category, amount, and date

## Module Structure

| File | Purpose |
|------|---------|
| `main.py` | Main application loop with menu interface |
| `add.py` | Add new expense functionality |
| `view.py` | View expenses filtered by month |
| `total.py` | Calculate total expenses for a month |
| `delete.py` | Delete expenses by date |
| `save.py` | Save budget and expenses to files |
| `load.py` | Load budget and expenses from files |

## Data Format

**expenses.csv:**
```
category,amount,date
Food,150.00,15/01/2026
Bills,200.50,20/01/2026
```

**budget.txt:**
```
5000.00
```

## Author

**Shikhar**

GitHub: https://github.com/ShikharPandey0170