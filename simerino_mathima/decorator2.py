# import random einai bibliothiki
import random


def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat_decorator(3)
def genarate_random_number():
    return random.randint(1, 10)


@repeat_decorator(2)
def greet(name):
    return f"hello,{name}!"


random_numbers = genarate_random_number()
greetings = greet("Alice")

print("Generated random numbers:", random_numbers)
print("Greetings", greetings)
