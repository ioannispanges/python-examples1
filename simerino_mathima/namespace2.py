def outer_function():
    y = 20

    def inner_function():
        print(y)

    inner_function()


outer_function()
