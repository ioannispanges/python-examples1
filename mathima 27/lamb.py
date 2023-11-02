class Lamp:
    def __init__(self, brand, is_on=False):
        self.brand = brand
        self.is_on = is_on

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
        return f"The {self.brand} lamb is now turned on"

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return f"The {self.brand} lamb is now turned off."
        else:
            return f"The {self.brand} lamb is already off"


my_lamp = Lamp("BrightLight")

print(my_lamp.turn_on())
print(my_lamp.turn_off())
print(my_lamp.turn_off())
print(my_lamp.turn_on())
