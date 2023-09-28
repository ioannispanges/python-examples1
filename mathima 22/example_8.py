import math

a = 1
b = -3
c = 2

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant) / (2 * a))
    x2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("The solutions are: ", x1, "and", x2)
elif discriminant == 0:
    x1 = -b / (2 * a)
    print("The solution is :", x1)
else:
    print("No real solutions")
