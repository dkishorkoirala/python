class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, Account):
            return Account(self.name, self.balance + other.balance)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Account):
            return Account(self.name, self.balance - other.balance)
        return NotImplemented

    def __eq__(self, value):
        if isinstance(value, Account):
            return self.balance == value.balance
        return NotImplemented

    def __gt__(self, value):
        if isinstance(value, Account):
            return self.balance > value.balance
        return NotImplemented

    def __lt__(self, value):
        if isinstance(value, Account):
            return self.balance < value.balance
        return NotImplemented

    def __str__(self):
        return f"Account {self.name}: ${self.balance}"


a1 = Account("Hari", 1000)
a2 = Account("Ram", 2000)

print(a1 + a2)
print(a1 - a2)
print(a1 == a2)
print(a1 > a2)
print(a1 < a2)
print(a1)

print(a1 + 5)
