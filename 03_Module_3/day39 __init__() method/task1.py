class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def display(self):
        print(f"Brand {self.brand} was launched in year {self.year}")
        
c1 = Car("BMW", 2023)
c2 = Car("Audi", 2022)

c1.display()
c2.display()