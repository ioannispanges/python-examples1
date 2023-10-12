def zero_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
         return " i diairesi den mborei na ginei"


result1 = zero_divide(10, 2)
result2 = zero_divide(10, 0)
print(result1)
print(result2)
