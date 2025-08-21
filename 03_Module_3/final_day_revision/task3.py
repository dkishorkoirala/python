class Wallet:
    def __init__(self):
        self.__money = 0

    def add_money(self, amount):
        self.__money += amount

    def get_money(self):
        return self.__money


w1 = Wallet()
w1.add_money(100)
print(w1.get_money())
