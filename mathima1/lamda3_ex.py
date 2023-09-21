def apply_operation(func, x, y):
    return func(x, y)


result = apply_operation(lambda a, b: a * b, 3, 4)
print(result)
