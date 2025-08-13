def make_sound(Animal):
    Animal.sound()


class Duck:
    def sound(self):
        print("Quack!")


class Cow:
    def sound(self):
        print("Boo!")


d = Duck()
c = Cow()

make_sound(d)
make_sound(c)
