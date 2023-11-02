class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


my_rectangle = Rectangle(5, 3)

print("Rectangle Area: ", my_rectangle.area())
print("Rectangle Perimeter,", my_rectangle.perimeter())
