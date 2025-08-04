class Shape:
    def area(self):
        print("Calculating area...")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()
        return f"Circle area: {3.14 * self.radius * self.radius}"


c = Circle(10)
print(c.area())
