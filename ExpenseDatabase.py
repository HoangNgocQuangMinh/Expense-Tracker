import sqlite3

conn = sqlite3.connect('ExpenseDatabase.db')

conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        expense_id TEXT PRIMARY KEY,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
""")

def add_expense(expense):
    with conn:
        conn.execute("""INSERT INTO expenses (expense_id, amount, category, description, date)
                        VALUES (:expense_id, :amount, :category, :description, :date)""",
                    {'expense_id': expense.expense_id,
                    'amount': expense.amount,
                    'category': expense.category,
                    'description': expense.description,
                    'date': expense.date
                    })


def get_expenses():
    with conn:
        cursor = conn.execute("SELECT * FROM expenses")
        return cursor.fetchall()

def get_expense_by_id(expense_id):
    with conn:
        cursor = conn.execute("""SELECT * FROM expenses WHERE expense_id = :expense_id""",
            {'expense_id': expense_id})
        return cursor.fetchone()

def update_expense(expense_id, amount):
    with conn:
        conn.execute("""UPDATE expenses SET amount = :amount WHERE expense_id = :expense_id""",
                    {'expense_id': expense_id, 'amount': amount})

def delete_expense(expense_id):
    with conn:
        conn.execute("""DELETE FROM expenses WHERE expense_id = :expense_id""", {'expense_id': expense_id})

def close_connection():
    conn.close()