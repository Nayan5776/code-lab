import csv
from datetime import datetime

FILENAME = "expenses.csv"
expenses = []

# ---------------- Load & Save Functions ----------------
def load_expenses():
    """Load expenses from CSV file"""
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass

def save_expenses():
    """Save expenses to CSV file"""
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["date", "amount", "category", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# ---------------- Core Functions ----------------
def add_expense():
    """Add a new expense"""
    try:
        amount = float(input("Enter amount (£): "))
        if amount <= 0:
            print("Amount must be positive.\n")
            return
    except ValueError:
        print("Invalid amount. Try again.\n")
        return

    category = input("Enter category (Food, Travel, etc.): ").strip()
    note = input("Enter note: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "amount": f"{amount:.2f}",
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expenses()
    print("✅ Expense added successfully!\n")

def view_expenses():
    """View all expenses"""
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nDate       | Amount (£) | Category   | Note")
    print("--------------------------------------------")
    for exp in expenses:
        print(f"{exp['date']} | {exp['amount']}     | {exp['category']} | {exp['note']}")
    print()

def total_expenses():
    """Show total amount spent"""
    if not expenses:
        print("No expenses recorded.\n")
        return
    total = sum(float(exp["amount"]) for exp in expenses)
    print(f"💰 Total Expenses: £{total:.2f}\n")

def filter_by_category():
    """Filter expenses by category"""
    cat = input("Enter category to filter: ").strip()
    filtered = [exp for exp in expenses if exp["category"].lower() == cat.lower()]
    if not filtered:
        print(f"No expenses found for category '{cat}'.\n")
        return

    print(f"\nExpenses for category '{cat}':")
    print("Date       | Amount (£) | Note")
    print("-------------------------------")
    for exp in filtered:
        print(f"{exp['date']} | {exp['amount']}     | {exp['note']}")
    print()

def monthly_summary():
    """Show total spent per month"""
    if not expenses:
        print("No expenses recorded.\n")
        return

    summary = {}
    for exp in expenses:
        month = exp["date"][:7]  # YYYY-MM
        summary[month] = summary.get(month, 0) + float(exp["amount"])

    print("\n📊 Monthly Summary:")
    for month, total in sorted(summary.items()):
        print(f"{month}: £{total:.2f}")
    print()

# ---------------- Menu ----------------
def show_menu():
    print("==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Filter by Category")
    print("5. Monthly Summary")
    print("6. Exit")

def main():
    load_expenses()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()