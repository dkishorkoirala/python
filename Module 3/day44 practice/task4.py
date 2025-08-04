class Products:
    discount = 0.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self):
        return self.price - (self.price * self.discount)


p1 = Products("Laptop", 50000)
print(p1.get_final_price())

Products.discount = 0.2
print(p1.get_final_price())
