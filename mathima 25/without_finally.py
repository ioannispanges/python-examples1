while True:
    numbers = int(input("Eisagete enan  arithmo ,1 gia to telos :"))
    try:
        result = 1 / numbers
    except ZeroDivisionError:
        print("Prosoxi: Diairesi me 0")
    else:
        print("O antistrofos tou arithmou", numbers, "einai:", result)
        if numbers == 1:
            break
    print("Telos Domis")
print("Telos programmatos")
