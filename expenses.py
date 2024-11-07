# expenses.py

# In-memory storage for expenses
expenses = []

def add_expense(user, date, amount, category, notes):
    """Adds an expense for a user."""
    expense = {
        "user": user,
        "date": date,
        "amount": amount,
        "category": category,
        "notes": notes
    }
    expenses.append(expense)

def get_expenses(user):
    """Retrieves all expenses for a specific user."""
    return [expense for expense in expenses if expense["user"] == user]

def update_expense(index, date, amount, category, notes):
    """Updates an existing expense by index."""
    expenses[index].update({
        "date": date,
        "amount": amount,
        "category": category,
        "notes": notes
    })

def delete_expense(index):
    """Deletes an expense by index."""
    expenses.pop(index)
