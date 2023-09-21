def add(a, b):
    return a + b


def subtrack(a, b):
    return a - b


def apply_operation(operation, x, y):
    return operation(x, y)


result1 = apply_operation(add, 3, 5)
result2 = apply_operation(subtrack, 10, 6)
print(result1)
print(result2)
