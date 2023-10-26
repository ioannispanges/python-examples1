try:
    numbers = int(input("Eisagete enan  arithmo :"))
    result = 1 / numbers
except (ZeroDivisionError, ValueError, KeyboardInterrupt, EOFError):
    print("Sfalma")
else:
    print("O antistrofos tou arithmou", numbers, "einai", result)
finally:
    print("Telos")
