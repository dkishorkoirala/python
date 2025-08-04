class BankAccount:
    interest_rate = 0.05

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def calculate_interest(self):
        return self.balance * self.interest_rate

    @classmethod
    def update_rate(cls, new_rate):
        cls.interest_rate = new_rate


a1 = BankAccount("Ram", 100000)
a2 = BankAccount("Sita", 200000)

print(a1.calculate_interest())
print(a2.calculate_interest())
print()
BankAccount.update_rate(0.1)
print(a1.calculate_interest())
print(a2.calculate_interest())
