def create_counter():
    count = 5

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def reset():
        nonlocal count
        count = 0
        return count

    def get_count():
        return count

    return increment, decrement, reset, get_count


increment_func, decrement_func, reset_func, get_count_func = create_counter()

print(increment_func())
print(increment_func())
print(decrement_func())
print(get_count_func())
print(reset_func())
print(get_count_func())



