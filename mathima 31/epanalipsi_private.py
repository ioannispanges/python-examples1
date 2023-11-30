class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()


obj = MyClass()

obj.public_method()
