try:
    exc_inside = True
    try:
        number = int(input("Eisagete enan arithmo:"))
    except KeyboardInterrupt:
        print("O xristis diekopse to programma")
    except EOFError:
        print("O xristis diekopse to EOF")
    except ValueError:
        print("Mi apodektos arithmos")
    else:
        exc_inside = False
        result = 1 / number
except ZeroDivisionError:
    print(" o arithmos 0 den exei antistrofo")
else:
    if exc_inside == False:
        print("O antistrofos tou arithmou", number, "einai:", result)
finally:
    print("Telos")
