class Mobile:
    def show(self):
        print(f"Brand: {self.brand}, Price: ${self.price}")

m = Mobile()

m.brand = "Apple"
m.price = 1000

m.show()