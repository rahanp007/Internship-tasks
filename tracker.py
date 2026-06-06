import json
import os
filename="expenses.json"

def load_expenses():
    if not os.path.exists(filename):
        return []
    with open(filename,"r") as f:
        return json.load(f)
    
def save_expenses(expenses):
    with open(filename,"w") as f:
        json.dump(expenses,f,indent=4)

def add_expense(category, amount):
    expenses=load_expenses()
    expense={
        "category":category,
        "amount":amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

def get_summary():
    expenses=load_expenses()

    summary={}

    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]

        summary[category]=summary.get(category, 0)+amount

    print("\nExpense Summary")
    print("-"*20)

    if not summary:
        print("no expenses found.")
        return
    for category, total in summary.items():
        print(f"{category}:{total}")


def view_all():
    expenses=load_expenses()

    print("\nAll Expenses")
    print("-",*20)

    if not expenses:
        print("No expenses  recorded")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}")