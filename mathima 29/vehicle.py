class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Doors: {self.num_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidebar):
        super().__init__(make, model)
        self.has_sidebar = has_sidebar

    def display_info(self):
        vehicle_info = super().display_info()
        sidebar_info = "with Sidecar" if self.has_sidebar else "without sidecar"
        return f"{vehicle_info}, Sidebar{sidebar_info}"


car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley", "Sportster", True)

print(car.display_info())
print(motorcycle.display_info())
