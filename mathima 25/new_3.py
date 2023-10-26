
try:
    numbers = int(input("Eisagete enan  arithmo :"))
    result = 1 / numbers
except (ZeroDivisionError, ValueError, KeyboardInterrupt, EOFError):
    for i in enumerate(ZeroDivisionError, ValueError):
        print(i)
    else:
        print("O antistrofos tou arithmou", numbers, "einai", result)
finally:
    print("Telos")