class Wizard:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level
        
    def cast_spell(self, target):
        print(f"{self.name} casts {self.power} on {target.name}!")
        
        
    def status(self):
        print(f"Name: {self.name}, power: {self.power}, Level: {self.level}")
        
w1 = Wizard("Harry Potter", "fire", 10)
w2 = Wizard("Hermione Granger", "lightning", 9)

w1.cast_spell(w2)
w2.cast_spell(w1)

w1.status()
w2.status()