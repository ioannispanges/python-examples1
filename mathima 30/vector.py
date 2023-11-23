class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


v1 = Vector2D (1, 2)
v2 = Vector2D (3, 5)

v3 = v1 + v2


print(v3.x, v3.y)
