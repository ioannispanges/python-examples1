class calculator:
    def __init__(self):
        self.result = 0

    # def exception(self, a, b):
    #     print(a,b)
    #     return ZeroDivisionError
    def add(self, a, b):
        self.result = a + b

    def substract(self, a, b):
        self.result = a - b

    def diaresi(self, a, b):
        self.result = 0
        try:
            self.result = a / b
        # except ZeroDivisionError:

        finally:
            self.result = ZeroDivisionError
            print("Not possible")

        # self.result = None

    def get_result(self):
        return self.result


my_calculator = calculator()

my_calculator.add(10, 10)
print("Result after addition", my_calculator.get_result())

my_calculator.substract(10, 3)
print("Result after sub", my_calculator.get_result())

my_calculator.diaresi(4, 0)
print("Result after diairesi", my_calculator.get_result())
