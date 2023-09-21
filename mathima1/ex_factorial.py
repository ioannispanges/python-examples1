def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = 5
print(f"the factorial of  {number} is {factorial_iter(number)}")
