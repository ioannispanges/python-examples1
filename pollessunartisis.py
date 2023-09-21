def john(func):
    def perform_operation(x, y):
        result = func(perform_operation)
        return result(x, y)

    return perform_operation


@john
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# result_add = (5, 3)
print(add)

# result_subtract = (10, 4)
print(subtract)
