class Animal:
    def make_sound(self):
        print("animal makes sound")


class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow!")


class Dog(Animal):
    def make_sound(self):
        print("Dog: Woof!")


a = Animal()
a.make_sound()

c = Cat()
c.make_sound()

d = Dog()
d.make_sound()
