class calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def substract(self, a, b):
        self.result = a - b

    def diaresi(self, a, b):
        self.result = a / b

    def get_result(self):
        return self.result


my_calculator = calculator()

my_calculator.add(10, 10)
print("Result after addition", my_calculator.get_result())

my_calculator.substract(10, 3)
print("Result after addition", my_calculator.get_result())

my_calculator.diaresi(0, 3)
print("Result after diairesi", my_calculator.get_result())
