class Myclass:
    def __init__(self):
        self.x = 10

    def get_x(self):
        return self.x


my_object1 = Myclass()
my_object2 = Myclass()

print(my_object1.x)
print(my_object2.x)

my_object1.x = 20
my_object2.x = 30

print(my_object1.x)
print(my_object2.x)
