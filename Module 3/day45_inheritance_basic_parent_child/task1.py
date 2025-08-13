class Animal:
    def sound(self):
        print("Some animal Sound")


class Dog(Animal):
    pass

    def bark(self):
        print("Woof")


d = Dog()
d.sound()
d.bark()
