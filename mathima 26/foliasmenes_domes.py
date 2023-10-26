try:
    number = int(input("Eisagete enan arithmo:"))
except KeyboardInterrupt:
    print("O xristis diekopse to programma")
except EOFError:
    print("O xristis diekopse to programma")
except ValueError:
    print("Mi apodektos arithmos")
else:
    try:
        result = 1 / number
    except ZeroDivisionError:
        print(" o arithmos 0 den exei antistrofo")
    else:
        print("O antistrofos tou arithmou", number, "einai:", result)
    finally:
        print("Telos")