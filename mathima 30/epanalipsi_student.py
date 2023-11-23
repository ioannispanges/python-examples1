class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} is enrolled in the {course} course")
        else:
            print(f"{self.name} is already enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} is unenrolled in the {course} course")
        else:
            print(f"{self.name} is not enrolled in the {course} course")

    def display_courses(self):
        if self.courses:
            print(f"{self.name}'s enrolled courses:{', '.join(self.courses)}")
        else:
            print(f"{self.name} is not currently enrolled in any courses")


student1 = Student("Alice", 20)
student1.add_course("History")
student1.add_course("Physics")
student1.display_courses()

student1.remove_course("Science")
student1.remove_course("Math")
student1.display_courses()
