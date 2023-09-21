def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 6
result = fibonacci(number)
print(f"The {number} in the Fibonacci is {result}")
