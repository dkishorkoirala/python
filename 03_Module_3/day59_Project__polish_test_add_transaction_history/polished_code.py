import random
from datetime import datetime

class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(Transaction(self.account_number, amount, "Deposit"))
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(Transaction(self.account_number, amount, "Withdrawal"))
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

    def show_transaction(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for t in self.transactions:
                print(t)

    def __str__(self):
        return f"{self.name} | Account: {self.account_number} | Balance: {self.balance}"


class Transaction:
    def __init__(self, account_number, amount, transaction_type):
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type} | Amount: {self.amount}"


# ------------------ MENU SYSTEM -------------------

accounts = {}


def main_menu():
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create a new account")
        print("2. Perform transaction")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            transaction_menu()
        elif choice == "3":
            print("Exiting the banking system. Thank you for using our service!")
            break
        else:
            print("Invalid choice. Please try again.")


def create_account():
    name = input("Enter your name: ")
    account_number = name[0].upper() + str(random.randint(100, 999))
    account = Account(name, account_number)

    choice = input("Do you want to deposit some money? (yes/no): ").lower()
    if choice == "yes":
        try:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid amount entered.")

    accounts[account_number] = account
    print("\nAccount created successfully!")
    print(account)  # Uses __str__


def transaction_menu():
    acc_num = input("Enter your account number: ")

    if acc_num not in accounts:
        print("Account not found.")
        return

    account = accounts[acc_num]

    while True:
        print("\n--- Transaction Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Show transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = int(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "2":
            try:
                amount = int(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transaction()

        elif choice == "5":
            print("Exiting transaction menu.")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()
