class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b

    def divide(self, a, b):
        if b != 0:
            self.result = a / b
        else:
            raise ZeroDivisionError("Division by zero is not allowed.")

    def get_result(self):
        return self.result


my_calculator = Calculator()

my_calculator.add(10, 10)
print("Result after addition:", my_calculator.get_result())

my_calculator.subtract(10, 3)
print("Result after subtraction:", my_calculator.get_result())

try:
    my_calculator.divide(3, 0)
    print("Result after division:", my_calculator.get_result())
except ZeroDivisionError as e:
    print("Error:", e)
