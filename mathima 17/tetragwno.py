def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def apply_function(func, numbers):
    return [func(num) for num in numbers]


numbers_list = [1, 2, 3, 4, 5]
squared_numbers = apply_function(square, numbers_list)
cubed_numbers = apply_function(cube, numbers_list)

print(squared_numbers)
print(cubed_numbers)
