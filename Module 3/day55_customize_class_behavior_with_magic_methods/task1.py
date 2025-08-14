class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Rectangle(self.width * factor, self.height * factor)
        return NotImplemented

    __rmul__ = __mul__

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Test
rect = Rectangle(2, 3)
rect2 = Rectangle(3, 4)
print(rect + rect2)
print(rect * 3)
print(3 * rect)
print(rect)
