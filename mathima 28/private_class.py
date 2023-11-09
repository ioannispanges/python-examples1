class myclass:
    def __init__(self):
        self.public_var = 42
        self._private_var = "I'm private"
        self.__mangled_var = "Name mangled"

    def public_method(self):
        print("This is public method")

    def _private_method(self):
        print("This is a private method")

    def __mangled_method(self):
        print("This is a name-mangled method")


obj = myclass()

print(obj.public_var)
obj.public_method()

print(obj._private_var)
obj._private_method()

print(obj._myclass__mangled_var)
obj._myclass__mangled_method()

