class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("John", 30)
person2 = Person("John", 30)

print(person1 == person2)
