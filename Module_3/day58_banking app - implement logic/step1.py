# step 1: skeleton code (basic structure)


class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass

    def show_transaction(self):
        pass


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
