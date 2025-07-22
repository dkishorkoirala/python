class Fruit:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is added")
    
    def __del__(self):
        print(f"{self.name} is removed")
        
f1 = Fruit("apple")
f2 = Fruit("banana")

del f1