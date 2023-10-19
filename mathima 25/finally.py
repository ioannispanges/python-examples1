number = int(input("Eisagete enan arithmo:"))
try:
    result = 1 / number
except ZeroDivisionError:
    print("O arithmos 0 den exei antistrofo")
else:
    print("o antistrofos tou arithmou", number, "einai", result)
finally:
    print("Telos")
