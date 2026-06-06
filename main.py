from tracker import add_expense,get_summary,view_all
def main():
    while True:
        print("\nExpense tracker")
        print("1. Add expense")
        print("2. View summary")
        print("3. View All Expenses")
        print("4. Exit")

        choice=input("Enter your choice")

        if choice=="1":
            category=input("Enter category:")
            amount=float(input("Enter Amount"))
            add_expense(category, amount)

        elif choice=="2":
            get_summary()

        elif choice=="3":
            view_all()
        
        elif choice=="4":
            print("Bye!")
            break
        else:
            print("Invalid Choice. Try Again.")

if __name__ =="__main__":
    main()