counter = 10


def increment_counter():
    global counter
    counter += 1


def print_counter():
    print("counter value: ", counter)


print_counter()
increment_counter()
increment_counter()
print_counter()
