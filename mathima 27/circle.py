class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius ** 2


circle1 = Circle(5)
circle2 = Circle(8)

print ("Value of Pi", Circle.pi)

print("Circle 1 - Radius:", circle1.radius)
print("Circle 1 -Area", circle1.calculate_area())


print("Circle 2 - Radius:", circle2.radius)
print("Circle 2 -Area", circle2.calculate_area())
