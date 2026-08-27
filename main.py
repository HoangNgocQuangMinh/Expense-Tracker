import sqlite3
import ExpenseDatabase
from ExpenseManager import ExpenseManager


ExpenseDatabase.initialize_database()

manager = ExpenseManager()


def display_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Find expense by ID")
    print("4. Update expense")
    print("5. Delete expense")
    print("6. Filter expenses by category")
    print("7. Filter expenses by date")
    print("8. View total expenses")
    print("9. View total by category")
    print("10. View total by date")
    print("0. Exit")


while True:
    display_menu()

    choice = input("Choose an option: ")

    match choice:
        case "0":
            print("Exiting Expense Tracker...")
            break

        case "1":
            print("You chose to Add expense!")
            print("Enter 0 to exit at any time if you changed your mind.")
            try:
                expense_id = input("Enter expense ID: ")
                if expense_id == "0":
                    continue
                amount = input("Enter amount: ")
                if amount == "0":
                    continue
                amount = float(amount)
                category = input("Enter category: ")
                if category == "0":
                    continue
                description = input("Enter description: ")
                if description == "0":
                    continue
                date = input("Enter date: ")
                if date == "0":
                    continue
                manager.add_expense(expense_id, amount, category, description, date)
                print("New expense added")

            except ValueError as e:
                print(f"Invalid input: {e}")

            except sqlite3.IntegrityError:
                print(f"Expense ID '{expense_id}' already exists!")

        case "2":
            print("You chose to View all expense!")

            expenses = manager.get_all_expenses()

            if not expenses:
                print("No expense found!")
            else:
                for expense in expenses:
                    print(expense)

        case "3":
            print("You chose to Find expense by ID!")
            print("Enter 0 to exit at any time if you changed your mind.")


            expense_id = input("Enter the ID you'd like to find: ")
            if expense_id == "0":
                continue
            expense = manager.get_expense_by_id(expense_id)

            if not expense:
                print(f"Expense not found with ID: {expense_id}")
            else:
                print("Expense found!")
                print(expense)

        case "4":
            print("You chose to Update expense!")
            print("Enter 0 to exit at any time if you changed your mind.")

            expense_id = input("Enter the expense ID you'd like to update: ")
            if expense_id == "0":
                continue

            expense = manager.get_expense_by_id(expense_id)
            if not expense:
                print(f"Expense not found with ID: {expense_id}")
                continue
            try:
                amount = input("Enter amount: ")
                if amount == "0":
                    continue
                amount = float(amount)
                category = input("Enter category: ")
                if category == "0":
                    continue
                description = input("Enter description: ")
                if description == "0":
                    continue
                date = input("Enter date: ")
                if date == "0":
                    continue

                manager.update_expense(expense_id, amount, category, description, date)

                print("Expense updated!")

            except ValueError as e:
                print(f"Invalid input: {e}")

        case "5":
            print("You chose to Delete expense!")
            print("Enter 0 to exit at any time if you changed your mind.")

            expense_id = input("Enter the expense ID you'd like to delete: ")
            if expense_id == "0":
                continue
            expense = manager.get_expense_by_id(expense_id)
            if not expense:
                print(f"Expense not found with ID: {expense_id}")
                continue

            manager.remove_expense(expense_id)
            print("Expense deleted!")

        case "6":
            print("You chose to Filter expenses by category!")
            print("Enter 0 to exit at any time if you changed your mind.")

            category = input("Enter the category which expenses you'd like to find: ")
            if category == "0":
                continue
            expenses = manager.filter_by_category(category)
            if not expenses:
                print(f"No expense found with category: {category}")
            else:
                for expense in expenses:
                    print(expense)
        case "7":
            print("You chose to Filter expenses by date!")
            print("Enter 0 to exit at any time if you changed your mind.")

            date = input("Enter the date which expenses you'd like to find: ")
            if date == "0":
                continue
            expenses = manager.filter_by_date(date)
            if not expenses:
                print(f"No expense found on: {date}")
            else:
                for expense in expenses:
                    print(expense)

        case "8":
            print("You chose to View total expenses!")
            try:
                total = manager.total_expense()
                print(f"Your total spending: {total} VND")
            except ValueError as e:
                print(e)

        case "9":
            print("You chose to View total by category!")
            print("Enter 0 to exit at any time if you changed your mind.")

            category = input("Enter category: ")
            if category == "0":
                continue
            try:
                total = manager.total_by_category(category)
                print(f"Your total spending for {category}: {total} VND")
            except ValueError as e:
                print(e)

        case "10":
            print("You chose to View total by date!")
            print("Enter 0 to exit at any time if you changed your mind.")

            date = input("Enter date: ")
            if date == "0":
                continue
            try:
                total = manager.total_by_date(date)
                print(f"Your total spending on {date}: {total} VND")
            except ValueError as e:
                print(e)
            
        case _:
            print("Invalid option. Please try again.")