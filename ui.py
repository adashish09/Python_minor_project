# ui.py

import tkinter as tk
from tkinter import messagebox, Canvas
from datetime import datetime
from auth import register_user, login_user
from expenses import add_expense, get_expenses
from visualization import plot_expenses_by_category, plot_expenses_over_time

# Define predefined categories for expenses
CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Health", "Other"]

def apply_gradient(canvas, width, height, color1, color2):
    """Applies a gradient background to a Tkinter canvas."""
    steps = 100  # Number of gradient steps
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps
    
    for i in range(steps):
        color = f'#{int(r1 + (r_ratio * i)):04x}{int(g1 + (g_ratio * i)):04x}{int(b1 + (b_ratio * i)):04x}'
        canvas.create_rectangle(0, i * (height // steps), width, (i + 1) * (height // steps), outline="", fill=color)

def auth_interface():
    """Authentication window for user login and registration."""
    
    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        if login_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            window.destroy()
            add_expense_interface(username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def handle_register():
        username = entry_username.get()
        password = entry_password.get()
        if register_user(username, password):
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Username already exists.")

    window = tk.Tk()
    window.title("Login / Register")
    window.geometry("500x400")  # Increased window size

    # Set up canvas for gradient background
    canvas = Canvas(window, width=500, height=400)
    canvas.pack(fill="both", expand=True)
    apply_gradient(canvas, 500, 400, "#4CAF50", "#2196F3")

    canvas.create_text(250, 60, text="Welcome to Expense Insight", font=("Arial", 18, "bold"), fill="white")
    canvas.create_text(250, 90, text="Personal Finance Tracker", font=("Arial", 18, "bold"), fill="white")


    # Username and Password fields with more spacing
    canvas.create_text(120, 150, text="Username:", font=("Arial", 12), fill="white")
    entry_username = tk.Entry(window, width=30, font=("Arial", 12))
    canvas.create_window(300, 150, window=entry_username)

    canvas.create_text(120, 200, text="Password:", font=("Arial", 12), fill="white")
    entry_password = tk.Entry(window, show="*", width=30, font=("Arial", 12))
    canvas.create_window(300, 200, window=entry_password)

    login_btn = tk.Button(window, text="Login", command=handle_login, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
    canvas.create_window(150, 270, window=login_btn)
    register_btn = tk.Button(window, text="Register", command=handle_register, bg="#2196F3", fg="white", font=("Arial", 12), width=15)
    canvas.create_window(350, 270, window=register_btn)

    window.mainloop()


def add_expense_interface(user):
    """Main interface for adding expenses and viewing visualizations."""
    
    def add_expense_callback():
        date = datetime.strptime(entry_date.get(), "%Y-%m-%d")
        amount = float(entry_amount.get())
        category = selected_category.get()
        notes = entry_notes.get()
        add_expense(user, date, amount, category, notes)
        messagebox.showinfo("Success", "Expense added successfully!")

    window = tk.Tk()
    window.title("Add Expense")
    window.geometry("800x800")  # Increased window size

    # Set up canvas for gradient background
    canvas = Canvas(window, width=800, height=800)
    canvas.pack(fill="both", expand=True)
    apply_gradient(canvas, 800, 800, "#FF9800", "#2196F3")

    canvas.create_text(250, 60, text="Add New Expense", font=("Arial", 18, "bold"), fill="white")

    # Date, Amount, Category, Notes fields with more spacing
    canvas.create_text(120, 130, text="Date (YYYY-MM-DD):", font=("Arial", 12), fill="white")
    entry_date = tk.Entry(window, width=30, font=("Arial", 12))
    canvas.create_window(350, 130, window=entry_date)

    canvas.create_text(120, 180, text="Amount:", font=("Arial", 12), fill="white")
    entry_amount = tk.Entry(window, width=30, font=("Arial", 12))
    canvas.create_window(350, 180, window=entry_amount)

    canvas.create_text(120, 230, text="Category:", font=("Arial", 12), fill="white")
    selected_category = tk.StringVar(window)
    selected_category.set(CATEGORIES[0])  # Default value
    category_dropdown = tk.OptionMenu(window, selected_category, *CATEGORIES)
    category_dropdown.config(width=26, font=("Arial", 12))
    canvas.create_window(350, 230, window=category_dropdown)

    canvas.create_text(120, 280, text="Notes:", font=("Arial", 12), fill="white")
    entry_notes = tk.Entry(window, width=30, font=("Arial", 12))
    canvas.create_window(350, 280, window=entry_notes)

    # Add and Visualization buttons with adjusted positions
    add_btn = tk.Button(window, text="Add Expense", command=add_expense_callback, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
    canvas.create_window(250, 340, window=add_btn)

    pie_chart_btn = tk.Button(window, text="Show Category Pie Chart", command=lambda: plot_expenses_by_category(user, get_expenses(user)), bg="#FF9800", fg="white", font=("Arial", 12), width=20)
    canvas.create_window(250, 390, window=pie_chart_btn)

    time_chart_btn = tk.Button(window, text="Show Spending Over Time", command=lambda: plot_expenses_over_time(user, get_expenses(user)), bg="#2196F3", fg="white", font=("Arial", 12), width=20)
    canvas.create_window(250, 440, window=time_chart_btn)

    window.mainloop()
