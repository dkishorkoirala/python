class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person({self.name!r})"


name = Person("Dibash")
print(name.name)
print(name)
print(repr(name))
