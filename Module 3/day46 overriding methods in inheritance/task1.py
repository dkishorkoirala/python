class Bird:
    def fly(self):
        print("Flying...")


class Penguin(Bird):
    def fly(self):
        print("I can't fly!")


p = Penguin()
p.fly()
