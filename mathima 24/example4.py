try:
    numerator = int(input("Eisagete enan arithmiti: "))
    denominator = int(input("Eisagete ena paranomasti: "))
    result = numerator / denominator
    print("Apotelesma", result)
except ZeroDivisionError:
    print("Error: Den epitrepetai i diairesi me to miden")
except ValueError:
    print("Error: Parakaloume eisagete egkires sto arithmiti i paranomasti ")
