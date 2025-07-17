class Animal:
    def make_sound(self):
        print(f"{self.name} {self.sound}")


anm = Animal()

anm.name = "Dog"
anm.sound = "barks"

anm.make_sound()

cat = Animal()

cat.name = "Cat"
cat.sound = "meows"

cat.make_sound()