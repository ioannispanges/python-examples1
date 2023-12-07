class MyClass:
    class_variable = 30

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def print_variable(self):
        print("Inside the method: class_variable= ", self.class_variable)
        print("Inside the method: instance_variable = ", self.instance_variable)


obj = MyClass(instance_variable=40)

print("Outside the instance (class attribute): class_variable=", MyClass.class_variable)

obj.print_variable()
