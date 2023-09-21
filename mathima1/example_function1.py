global_var = 10


def example_function1():
    local_vars = locals()
    global_vars = globals()
    print(local_vars)
    print(global_vars)


example_function1()
