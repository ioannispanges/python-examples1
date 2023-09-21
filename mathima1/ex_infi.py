def infinite():
    n = 1
    while True:
        yield n
        n += 1


counter = 0
for number in infinite():
    print(number)
    counter += 1
    if counter >= 10:
        break
