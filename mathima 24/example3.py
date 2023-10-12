number = int(input('Έισάγετε έναν αριθμο :'))
try:
    result = 1 / number
    print("Ο αντίστροφος του αριθμού", number, "ειναι:", result)
except ZeroDivisionError:
    print(" Ο αριθμος πρέπει να ειναι διάφορος του μηδενός")
print("The End")
