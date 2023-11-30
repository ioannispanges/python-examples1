class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point{self.x},{self.y}"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)


point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(1, 2)

print(point1 == point2)
print(point1 == point3)

print(point1 > point2)
print(point1 < point3)

# points = [point1, point2, point3]
# sorted_points = sorted(points)
# print("Sorted Points", sorted_points)
