from functools import reduce
from datetime import datetime

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gobipydev@22",
    database="expense_management_system"
)

cursor = conn.cursor()

def get_cursor():
    return conn.cursor()

''' USER creation '''

class User:
    def __init__(self, name):
        self.name = name
    
    def add_user(self):
        cursor = get_cursor()
        cursor.execute("INSERT INTO users(name) VALUES (%s)", (self.name,))
        conn.commit()
        return cursor.lastrowid
    
class Expense(User):
    def __init__(self, name):
        super().__init__(name)

    def add_expense(self, user_id, amount, category, description, date):
        cursor = get_cursor()
        cursor.execute(
            "INSERT INTO expense(user_id, amount, category, description, date) VALUES (%s, %s, %s, %s, %s)",
            (user_id, amount, category, description, date),
        )
        conn.commit()
        return cursor.lastrowid

print("committed successful")


# viewing All Expenses

def view_expenses(user_id):
    cursor = get_cursor()
    cursor.execute("""
    SELECT users.name, expense.amount, expense.category, expense.description, expense.date
    FROM expense
    JOIN users ON users.user_id = expense.user_id
    WHERE users.user_id = %s
    """, (user_id,))
    return cursor.fetchall()


# Filtering the Expenses

def filter_by_category(expense, catogory):
    return list(filter(lambda x:x[2]==catogory,expense))


def filter_by_date(expense, date):
    return [exp for exp in expense if exp[4] == date]



# total expenses
def total_expense(expense):
    amount = list(map(lambda x:x[1],expense))
    return reduce(lambda a,b : a+b, amount)

# Category wise spending

def category_wise(expense):
    categories = {exp[2]: 0 for exp in expense}
    for exp in expense:
        categories[exp[2]] += exp[1]
    return categories

#delete expense

def delete_expense(exp_id):
    cursor = get_cursor()
    cursor.execute("DELETE FROM expense WHERE exp_id = %s", (exp_id,))
    conn.commit()

# update expense
def UPDATE_expense(exp_id, amount, category, description, date):
    cursor = get_cursor()
    cursor.execute(
        "UPDATE expense SET amount = %s, category = %s, description = %s, date = %s WHERE exp_id = %s",
        (amount, category, description, date, exp_id),
    )
    conn.commit()

#highest Expense

def highest_expense(expense):
    return reduce(lambda a,b : a if a[1] > b[1] else b, expense)

def monthly_report(expense):
    report = {}

    for exp in expense:
        exp_date = exp[4]
        if isinstance(exp_date, str):
            exp_date = datetime.strptime(exp_date, "%Y-%m-%d")
        month = exp_date.strftime("%Y-%m")

        if month not in report:
            report[month] = 0
        report[month] += exp[1]

    return report


def smart_insight(expense):
    category_totals = category_wise(expense)
    max_cat = max(category_totals, key=category_totals.get)
    print(f"You are spending too much on {max_cat} this month")


# Adding user data

if __name__ == "__main__":
    u1 = Expense("Alice")
    user_id = u1.add_user()

    u1.add_expense(user_id, 2000, "Food", "Lunch at restaurant", "2024-06-01")
    u1.add_expense(user_id, 3500, "Travel", "Flight tickets", "2024-09-01")
    u1.add_expense(user_id, 1500, "Shopping", "New Dresses", "2024-08-01")

    expenses = view_expenses(user_id)
    print(total_expense(expenses))
    print(category_wise(expenses))
    print(highest_expense(expenses))
    smart_insight(expenses)

