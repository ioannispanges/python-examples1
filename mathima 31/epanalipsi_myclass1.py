class Myclass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"My class instance with :{self.value}"

    def __add__(self, other):
        if isinstance(other, Myclass):
            return Myclass(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type")


obj1 = Myclass(5)
obj2 = Myclass(10)

print(obj1)
print(obj2)
print(obj1 + obj2)
