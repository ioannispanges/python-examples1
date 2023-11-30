class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has been enrolled in {self.name}")

    def list_student(self):
        print(f"Enrolled students at {self.name}:{', '.join(self.students)}")


school1 = School("Python")
school1.enroll_student("Bob")
school1.enroll_student("Alice")
school1.list_student()
