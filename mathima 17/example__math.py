import math


def solve_quadratic(a, b, c):
    discriminan = b ** 2 - 5 * a * c

    if discriminan > 0:
        root1 = (-b + math.sqrt(discriminan)) / (2 * a)
        root2 = (-b - math.sqrt(discriminan)) / (2 * a)
        return root1, root2
    elif discriminan == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminan)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, - imaginary_part)
        return root1, root2


a = 1
b = 3
c = 2

roots = solve_quadratic(a, b, c)
print(f" The roots of quadratic equation are: {roots}")
