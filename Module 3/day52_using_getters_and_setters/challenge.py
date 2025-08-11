class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return f"Initial Balance: {self.__balance}"

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New Balance: {self.__balance}"
        else:
            return "Error: Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Withdrawal successful. New Balance: {self.__balance}"
        else:
            return "Error: Insufficient funds."

    def f_balance(self):
        return f"Final Balance: {self.__balance}"


acc = BankAccount(500)
print(acc.balance)
print(acc.deposit(300))
print(acc.deposit(-1))
print(acc.withdraw(300))
print(acc.withdraw(600))
print(acc.f_balance())
