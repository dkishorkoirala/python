class Wizard:
    def set_name(self, name):
        self.name = name
    
    def cast_spell(self, target):
        print(f"{self.name} casts a spell on {target.name}")


w1 = Wizard()
w2 = Wizard()

w1.set_name("Harry Potter")
w2.set_name("Hermione Granger")

w1.cast_spell(w2)