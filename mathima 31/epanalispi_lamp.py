class Lamp:
    def __init__(self, brand, is_on=False):
        self.brand = brand
        self.is_on = is_on

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            return f"The {self.brand} lamp is now turned on"
        else:
            return f"The {self.brand} lamp is already on"

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return f"The {self.brand} lamp is now turned off"
        else:
            return f"The {self.brand} lamp is already off"


my_lamp = Lamp("Bright")

print(my_lamp.turn_on())
print(my_lamp.turn_off())
print(my_lamp.turn_off())
print(my_lamp.turn_on())
