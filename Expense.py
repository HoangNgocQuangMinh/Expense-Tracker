import datetime

class Expense:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    @property
    def expense_id(self):
        return self._expense_id
    
    @expense_id.setter
    def expense_id(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong input!!!")
        self._expense_id = value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Wrong input!!!")
        if value < 0:
            raise ValueError("Amount cannot be smaller than 0")
        self._amount = value
    
    def __str__(self):
        return(f"Expense ID: {self.expense_id}\n"
                f"Amount: {self.amount:,}$\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Date: {self.date}")