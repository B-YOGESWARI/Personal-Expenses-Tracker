import json
import datetime

FILE = "expenses.json"

# Load expenses
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses
def save_expenses(expenses):
    with open(FILE, "w") as f:

        json.dump(expenses, f, indent=4)

# Add expense
def add_expense(expenses):
    
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Invalid amount!")
            return
    except ValueError:
        print("Enter a valid number!")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    expenses.append({"id": len(expenses) + 1, "category": category, "amount": amount, "date": date})
    save_expenses(expenses)
    print("Expense added!")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n Expenses:")
    for exp in expenses:
        print(f"ID: {exp['id']}, Category: {exp['category']}, ₹{exp['amount']}, Date: {exp['date']}")
    print(f" Total: ₹{sum(exp['amount'] for exp in expenses)}")

# Delete expense
def delete_expense(expenses):
    try:
        exp_id = int(input("Enter Expense ID to delete: "))
    except ValueError:
        print(" Invalid ID!")
        return

    for exp in expenses:
        if exp["id"] == exp_id:
            expenses.remove(exp)
            save_expenses(expenses)
            print("Expense deleted!")
            return
    print(" ID not found!")
#Menu
def main():
    expenses = load_expenses()
    while True:
        print("\n Expense Tracker\n 1. Add Expense\n 2. View Expenses\n 3. Delete Expense\n 4.Exit")
        choice = input("Choose (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print(" Exiting...")
            break
        else:
            print(" Invalid choice!")
# Run
if __name__ == "__main__":
    main()