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
            raise TypeError("Expense ID must be a string!")
        self._expense_id = value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Amount must be number!")
        if value <= 0:
            raise ValueError("Invalid amount of money")
        self._amount = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string!")
        self._category = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string!")
        self._description = value    

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Date must be a string!")
        self._date = value 
    
    def __str__(self):
        return(f"Expense ID: {self.expense_id}\n"
                f"Amount: {self.amount:.2f} VND\n"
                f"Category: {self.category}\n"
                f"Description: {self.description}\n"
                f"Date: {self.date}")