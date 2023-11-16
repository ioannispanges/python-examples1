class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


cars = {}

cars["my_car"] = Car("Toyota", "Corolla", 2023)
cars["my_car1"] = Car("Opel", "Corsa", 2017)

# print(cars['my_car'].make)
# print(cars['my_car'].model)
# print(cars['my_car'].year)


# cars["my_car"].make = "Honda"

for car_name, car_instance in cars.items():
    print(f"{car_name}: {car_instance.make} {car_instance.model} ({car_instance.year})")
