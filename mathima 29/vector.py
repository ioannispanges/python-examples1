class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector{self.x}, {self.y}"

    def __repr__(self):
        return f"Vector{self.x}, {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __del__(self):
        return f"Vector ({self.x}, {self.y}) has been deleted"

    def __call__(self):
        return self.magnitude()

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)
print(repr(v1))
print(v1 + v2)
print(v1 - v2)
print(v1 == v2)
print(v1())

del v1
