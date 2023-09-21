def john(func):
    def perform_operation(x, y):
        result = func(x, y)
        return result

    return perform_operation


@john
def add(a, b):
    return a + b


@john
def subtract(a, b):
    return a - b


result_add = add(5, 3)
result_subtract = subtract(10, 4)

print(result_add)  # Output: 8
print(result_subtract)  # Output: 6
