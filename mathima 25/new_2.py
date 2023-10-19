try:
    numbers = int(input("Eisagete enan  arithmo :"))
    result = 1 / numbers
except KeyboardInterrupt:
    print("O xristis diekopse to programma")
except EOFError:
    print("O xristis pliktrologise telos tou arxeiou")
except ZeroDivisionError:
    print("O arithmos 0 den exei antistrofo")
except ValueError:
    print("Mi apodektos arithmos")
else:
    print("O antistrofos tou arithmou", numbers, "einai", result)
finally:
    print("Telos")
