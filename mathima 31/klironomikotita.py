class Animal:
    def __init__(self, nane):
        self.name = nane

    def speak(self):
        print("Some generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")

    def wag_tail(self):
        print("Tail is wagging.")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog_instance = Dog(nane="Buddy")
cat_instance = Cat(nane="Whiskers")

print(f"{dog_instance.name} says:")
dog_instance.speak()
dog_instance.wag_tail()

print(f"{cat_instance.name} says:")
cat_instance.speak()
