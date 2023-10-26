class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


student1 = Student("Alice", 18, 11)
student2 = Student("Bob", 15, 10)

print(f"{student1.name} is {student1.age} years old and is in grade {student1.grade}.")
print(f"{student2.name} is {student2.age} years old and is in grade {student2.grade}.")

student1.display_info()
student2.display_info()
