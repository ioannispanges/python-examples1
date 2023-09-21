def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello,{name}"


@uppercase_decorator
def say_goodbye(name):
    return f"Goodbye, {name}"


print(greet("Alice"))
print(say_goodbye("Bob"))
