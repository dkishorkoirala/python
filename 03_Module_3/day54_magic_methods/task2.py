class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - ${self.price}"

    def __repr__(self):
        return f"Product({self.name!r},{self.price})"


product1 = Product("Laptop", 1000)
print(product1)
print(repr(product1))
