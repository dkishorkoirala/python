class Cat:
    def set_name(self, name):
        self.name = name

    def meow(self):
        print(f"Meow, I'm {self.name}.")

cat1 = Cat()
cat2 = Cat()

cat1.set_name("Sade")
cat2.set_name("Luna")

cat1.meow()
cat2.meow()