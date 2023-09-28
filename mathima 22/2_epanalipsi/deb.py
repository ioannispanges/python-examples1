def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    return result


numerator = 10
demomirator = 2
result = divide(numerator, demomirator)

print(f"The result of {numerator} / {demomirator} is: ", result)
