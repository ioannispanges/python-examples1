def outer():
    outer = 40

    def inner():
        print(outer)

    inner()


outer()
