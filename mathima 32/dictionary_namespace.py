class NamespaceClass:
    def __init__(self):
        self.namespace = {}

    def add_attribute(self, key, value):
        self.namespace[key] = value

    def get_attribute(self, key):
        return self.namespace.get(key, None)

    def print_namespace(self):
        print("Namespace", self.namespace)


my_instance = NamespaceClass()

my_instance.add_attribute('variable1', 10)
my_instance.add_attribute('variable2', "Hello, World!")

my_instance.print_namespace()

print("Accessing variable: ", my_instance.get_attribute('variable1'))

my_instance.add_attribute('variable1', 20)

my_instance.print_namespace()

print("Modified variable:", my_instance.get_attribute('variable1'))

print("Accessing non-existent variable3:", my_instance.get_attribute('variable3'))
