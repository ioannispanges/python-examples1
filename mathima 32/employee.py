class Employee:
    def __init__(self, employee_id, name, base_salary):
        self.employee_id = employee_id
        self.name = name
        self._base_salary = base_salary

    def calculate_salary(self):
        return self._base_salary

    def __str__(self):
        return f"Employee # {self.employee_id} - {self.name}"


class Manager(Employee):
    def __init__(self, employee_id, name, base_salary, bonus_percentage):
        super().__init__(employee_id, name, base_salary)
        self._bonus_percentage = bonus_percentage

    def __str__(self):
        return f"Manager # {self.employee_id} - {self.name}"


class Intern(Employee):
    def __init__(self, employee_id, name, base_salary, duration_weeks):
        super().__init__(employee_id, name, base_salary)
        self._duration_weeks = duration_weeks

    def calculate_salary(self):
        return self._base_salary / 4 * self._duration_weeks

    def __str__(self):
        return f"Intern # {self.employee_id} - {self.name}"


employee1 = Employee(1, "John Doe", 50000)
manager1 = Manager(2, "Jane Smith", 80000, 15)
intern1 = Intern(3, "Alex Johnson", 20000, 12)

employees = [employee1, manager1, intern1]

for employee in employees:
    print(employee)
    print(f" Monthly Salary: {employee.calculate_salary()}")
