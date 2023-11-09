class Dog:
    species = "Canine"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species


dog1 = Dog("Budy", 3)
print(dog1.description())
print("Species of dog1 ", dog1.species)

dog2 = Dog("Moly", 7)
print(dog1.description())
print("Species of dog1 ", dog2.species)

Dog.set_species("Wolf")
print("Species of dog 1 after species change", dog1.species)
print("Species of dog 2 after species change", dog2.species)


