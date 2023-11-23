class Animal:
    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()
