# step 2 : implementing account methods


class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(self.account_number, amount, "Deposit"))
        print(f"Deposit {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(
                Transaction(self.account_number, amount, "Withdrawal")
            )
            print(f"Withdrawal {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

    def show_transaction(self):
        if not self.transactions:
            print("No transactions yet.")

        else:
            for t in self.transactions:
                print(f"{t.transaction_type}: {t.amount}")


class Transaction:
    def __init__(self, account_number, amount, transaction_type):
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type


# ------------------menu-------------------

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
            print("Exiting the banking system, Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


def create_account():
    pass


def transaction_menu():
    pass


main_menu()
