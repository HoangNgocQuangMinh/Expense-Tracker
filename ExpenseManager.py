import ExpenseDatabase
from Expense import Expense

class ExpenseManager:

    def add_expense(self, expense_id, amount, category, description, date):
        expense = Expense(expense_id = expense_id,
                          amount = amount,
                          category = category,
                          description = description,
                          date = date)
        ExpenseDatabase.add_expense(expense)
        return expense
        
    def get_all_expenses(self):
        return ExpenseDatabase.get_expenses()

    def get_expense_by_id(self, expense_id):
        return ExpenseDatabase.get_expense_by_id(expense_id)

    def update_expense(self, expense_id, amount = None, category = None, description = None, date = None):
        expense = self.get_expense_by_id(expense_id)
        if not expense:
            raise ValueError(f"Expense not found with ID: {expense_id}")
        if amount is not None:
            expense.amount = amount
        if category is not None:
            expense.category = category
        if description is not None:
            expense.description = description
        if date is not None:
            expense.date = date
        ExpenseDatabase.update_expense(expense)
        return expense
        
    def remove_expense(self, expense_id):
        return ExpenseDatabase.delete_expense(expense_id)

    def filter_by_category(self, category):
        return ExpenseDatabase.get_expense_by_category(category)

    def filter_by_date(self, date):
        return ExpenseDatabase.get_expense_by_date(date)

    def total_expense(self):
        expenses = self.get_all_expenses()
        if not expenses:
            raise ValueError("Expenses not found")
        return sum(expense.amount for expense in expenses)
        
    def total_by_category(self, category):
        expenses = self.filter_by_category(category)
        if not expenses:
            raise ValueError("Expenses not found")
        return sum(expense.amount for expense in expenses)

    def total_by_date(self, date):
        expenses = self.filter_by_date(date)
        if not expenses:
            raise ValueError("Expenses not found")
        return sum(expense.amount for expense in expenses)