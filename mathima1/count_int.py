def count_integers(start=1):
    while True:
        yield start
        start += 1


counter = count_integers(5)
for _ in range(5):
    print(next(counter))
