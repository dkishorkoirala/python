class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1


d1 = Dog("Tommy")
d2 = Dog("Bruno")

print(Dog.total_dogs)
