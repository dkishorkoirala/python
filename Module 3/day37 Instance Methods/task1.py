class Player:
    def cheer(self):
        print(f"Let's go, {self.name}!")

p = Player()
p.name = "John"
p.cheer()