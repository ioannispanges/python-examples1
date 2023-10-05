def divide_and_remainder(divident, divisor, a, b):
    quotient = divident // divisor
    remainder = divident % divisor

    add = a + b
    return quotient, remainder, add


q, r, add = divide_and_remainder(10, 3, 2,3 )
print("Quotient", q)
print("Remainder", r)
print(add)
