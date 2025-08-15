class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scaler):
        if isinstance(scaler, (float, int)):
            return Vector(self.x * scaler, self.y * scaler)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector1 + vector2
print(vector3)
print(vector1 * 2)
