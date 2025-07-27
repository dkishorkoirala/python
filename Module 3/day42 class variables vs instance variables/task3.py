class Products:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Products("Laptop", 50000)
p2 = Products("Mobile", 30000)

print(p1.name, p1.price, p1.category)


Products.category = "Tech"
print()
print(p2.name, p2.price, p2.category)

p3 = Products("Tablet", 20000)
p3.category = "MODERN Tech"
print()
print(p3.name, p3.price, p3.category)
