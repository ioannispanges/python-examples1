try:
    numbers = int(input("Eisagete enan arithmo: "))
    result = 1 / numbers
except (ZeroDivisionError, ValueError, KeyboardInterrupt, EOFError) as e:
    for i, error in enumerate([ZeroDivisionError, ValueError, KeyboardInterrupt, EOFError]):
        if isinstance(e, error):
            print(i, error)
else:
    print("O antistrofos tou arithmou", numbers, "einai", result)
finally:
    print("Telos")
