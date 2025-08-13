from tracker import add_expense, show_expenses

while True: 
    print("\n\nOPTIONS are\n1. Add Expenses\n2.View all expenses\n3. Exit")

    choice = int(input("\nEnter your choice(numbers only): "))

    if choice == 1:
        amount = int(input("Enter your amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)

    elif choice == 2:
        print(show_expenses())

    elif choice == 3:
        print("Thank you for your visit....")
        break
    else:
        print("Invalid choice")