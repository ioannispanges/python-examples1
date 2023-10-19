numbers = int(input("Eisagete enan  arithmo:"))
try:
    result = 1 / numbers
    print("O antistrofos tou arithmou", numbers, "einai:", result)

except ZeroDivisionError:
    print("Prosoxi: Diairesi me 0")

finally:
    print("Telos Domis")
