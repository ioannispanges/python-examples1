class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.khm = 110

    def display_info(self):
        print(f" Make: {self.make}, Model: {self.model}, Year:{self.year}, Color:{self.color},Khm :{self.khm}")
        print(f" Xiliometra: {self.khm}")
        print(f"Driving {self.khm} xiliometra")

    def drive(self, khm):
        self.khm += khm
        print(f"Driving{self.khm} xiliometra.")


car1 = Car("Toyota", "Aygo", 2023, "Blue")
car2 = Car("Opel", "Corsa", 2023, "White")

car1.display_info()
car2.display_info()
#
car1.drive(100)
car2.drive(90)
