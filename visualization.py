# visualization.py

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import matplotlib.dates as mdates

def plot_expenses_by_category(user, expenses):
    """Plots a pie chart of expenses by category for a user."""
    user_expenses = [e for e in expenses if e["user"] == user]
    categories = [expense["category"] for expense in user_expenses]
    category_counts = Counter(categories)
    
    labels = category_counts.keys()
    sizes = category_counts.values()

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Spending by Category")
    plt.show()

def plot_expenses_over_time(user, expenses):
    """Plots a line chart showing cumulative spending over time for a user."""
    user_expenses = sorted([e for e in expenses if e["user"] == user], key=lambda x: x["date"])

    dates = [expense["date"] for expense in user_expenses]
    amounts = np.cumsum([expense["amount"] for expense in user_expenses])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o', color='b')
    plt.xlabel("Date")
    plt.ylabel("Cumulative Spending")
    plt.title("Spending Over Time")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gcf().autofmt_xdate()
    plt.show()
