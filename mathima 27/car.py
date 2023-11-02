class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def _start_engine(self):  # protected
        print("Engine started for", self._make, self._model)

    def drive(self):
        self._start_engine()
        print("Driving the", self._make, self._model)


my_car = Car('Toyota', 'Corolla')

print("Accessing to protected attributes:")
print(my_car._make)
print(my_car._model)

print("Accessing protected method:")
my_car.drive()
