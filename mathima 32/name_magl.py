class MyClass:
    def __init__(self):
        # dimosia klassi
        self.public_variable = 10
        # name-mangled variable
        self.__mangled_variable = 20

    def get_mangled_variable(self):
        #         prosbasi sti mangled methodos
        return self.__mangled_variable


obj = MyClass()

print("Public variable", obj.public_variable)

print("Mangled variable (via method)", obj.get_mangled_variable())
