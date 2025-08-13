class Animal:
    def sound(self):
        print("some generic animal sound")


class Lion(Animal):
    def sound(self):
        super().sound()
        print("Lion: Roar!")


l1 = Lion()
l1.sound()
