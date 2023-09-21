def factorial_re(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_re(n - 1)


number = 6
print(f"The factorial of {number} is {factorial_re(number)}")
