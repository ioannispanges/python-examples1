def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_5 = outer_function(5)
add_10 = outer_function(10)

result1 = add_5(5)
result2 = add_10(3)

print(result1)
print(result2)
