from contextlib import contextmanager
import sqlite3

from Expense import Expense

@contextmanager
def get_connection():
    conn = sqlite3.connect('ExpenseDatabase.db')

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def initialize_database():
    with get_connection() as conn:
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
    with get_connection() as conn:
        conn.execute("""INSERT INTO expenses (expense_id, amount, category, description, date)
                        VALUES (:expense_id, :amount, :category, :description, :date)""",
                    {'expense_id': expense.expense_id,
                    'amount': expense.amount,
                    'category': expense.category,
                    'description': expense.description,
                    'date': expense.date
                    })


def get_expenses():
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

        return [
            Expense(
            expense_id = row[0],
            amount = row[1],
            category = row[2],
            description = row[3],
            date = row[4])
        for row in rows
            ]

def get_expense_by_id(expense_id):
    with get_connection() as conn:
        cursor = conn.execute("""SELECT * FROM expenses WHERE expense_id = :expense_id""",
            {'expense_id': expense_id})
        row = cursor.fetchone()

        if row is None:
            return None
        return Expense(
            expense_id = row[0],
            amount = row[1],
            category = row[2],
            description = row[3],
            date = row[4])

def update_expense(expense):
    with get_connection() as conn:
        cursor = conn.execute("""UPDATE expenses
                    SET amount = :amount, category = :category, description = :description, date = :date
                    WHERE expense_id = :expense_id""",
                    {'expense_id': expense.expense_id, 
                    'amount': expense.amount, 
                    'category': expense.category,
                    'description': expense.description,
                    'date': expense.date})
        return cursor.rowcount

def delete_expense(expense_id):
    with get_connection() as conn:
        cursor = conn.execute("""DELETE FROM expenses WHERE expense_id = :expense_id""",
                            {'expense_id': expense_id})
        return cursor.rowcount

def get_expense_by_category(category):
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses WHERE category = :category",
                              {'category': category})
        rows = cursor.fetchall()

        return [ Expense(
            expense_id = row[0],
            amount = row[1],
            category = row[2],
            description = row[3],
            date = row[4])
        for row in rows]

def get_expense_by_date(date):
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses WHERE date = :date",
                              {'date': date})
        rows = cursor.fetchall()

        return [ Expense(
            expense_id = row[0],
            amount = row[1],
            category = row[2],
            description = row[3],
            date = row[4])
        for row in rows]