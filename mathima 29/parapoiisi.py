class Myclass:
    def __init__(self):
        self.__x = 10

    def __hidden_method(self):
        print("This is private")


class MySubClass(Myclass):
    def print_x(self):
        print(self._Myclass__x)

    def call_hidden_method(self):
        self._Myclass__hidden_method()


obj = MySubClass()

try:
    print(obj._Myclass__x)
except AttributeError as e:
    print(e)

try:
    obj._Myclass__hidden_method()
except AttributeError as e:
    print(e)
