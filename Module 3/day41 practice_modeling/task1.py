class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
    
    def specs(self):
        print(f"Brand: {self.brand}\nRam: {self.ram}\nStorage: {self.storage}")
        

l1 = Laptop("Dell", "16GB", "1TB")
l2 = Laptop("Asus", "8GB", "500GB")

l1.specs()
l2.specs()