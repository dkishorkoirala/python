class Pen:
    def write(self):
        print(f"Writing in {self.color} with {self.brand}")


p = Pen()
p.brand = "Reynolds"
p.color = "Blue"

p.write()