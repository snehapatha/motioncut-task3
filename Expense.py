class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Date\t\tCategory\tAmount")
            for expense in self.expenses:
                print(f"{expense.date}\t{expense.category}\t\t${expense.amount}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: ${total}")

    def expenses_for_category(self, category):
        category_total = sum(expense.amount for expense in self.expenses if expense.category == category)
        print(f"Total expenses for {category}: ${category_total}")

# Example usage:
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Calculate Expenses for a Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            expense = Expense(date, category, amount)
            tracker.add_expense(expense)
            print("Expense added successfully!")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.total_expenses()

        elif choice == '4':
            category = input("Enter category to calculate expenses: ")
            tracker.expenses_for_category(category)

        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
