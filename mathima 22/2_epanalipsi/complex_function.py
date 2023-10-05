def complex_function(name, *args, greeting="Hello", **kwargs):
    return f"{greeting}, {name} Args:{args}, Kwargs:{kwargs}"


result = complex_function("Alice", 1, 2, 3, country="USA", age=35)
print(result)