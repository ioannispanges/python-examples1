class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Name: {self.name}, Employee_id:{self.employee_id}"


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_info(self):
        emp_info = super().display_info()
        return f"{emp_info}, Department {self.department}"


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_info(self):
        emp_info = super().display_info()
        return f"{emp_info}, Language {self.programming_language}"


manager = Manager("Alice Doe", "M123", "Engineering")
developer = Developer("Bob Doe", "D865", "Python")

print(manager.display_info())
print(developer.display_info())
