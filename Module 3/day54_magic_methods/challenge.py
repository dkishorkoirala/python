class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - ${self.price}"

    def __repr__(self):
        return f"Product({self.name!r},{self.price})"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Shopping Cart with {len(self)} items"

    def __repr__(self):
        return f"ShoppingCart({self.items!r})"

    def add_product(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(p.price for p in self.items)


cart = ShoppingCart()
cart.add_product(Product("Laptop", 1000))
cart.add_product(Product("Mouse", 50))

print(cart)  # __str__
print(repr(cart))
print("Total price:", cart.total_price())
print("Items in cart:", len(cart))
