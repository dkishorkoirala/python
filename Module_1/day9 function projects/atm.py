#smart ATM system:
balance = 1000
pin = "1234"
attempt = 3

while attempt>0:
    ask = input("Enter your 4-digit pin: ")
    if ask == pin:
        print("Welcome to the ATM system!")
    else:
        attempt -= 1
        print("Incorrect PIN. You have", attempt, "exhausted attempts remaining.")
else:
    print("You have exhausted all attempts. Your account has been locked.")
    exit()

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Print Receipt")
    print("5. Exit")

    chose= int(input("Enter your choice: "))

    if chose == 1:
        print(f"Your balance is {balance}")
    elif chose == 2:
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw
            print(f"Withdrawn {withdraw}. Your new balance is {balance}")
    
    elif chose == 3:
        deposit = int(input("Enter the amount to deposit: "))
        balance += deposit
        print(f"Deposited {deposit}. Your new balance is {balance}")
    elif chose == 4:
        print("Your receipt:")
        print("----------------")
        print("Transaction complete")
        print(f"Remaining balance is {balance}")
        print("Thank you for using our ATM")
        print("----------------")
    elif chose == 5:
        print("Thank you for using our smart ATM system!")
        break
    else:
        print("Invalid choice... ")
    
