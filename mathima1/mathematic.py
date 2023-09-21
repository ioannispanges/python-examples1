import math

name = "John"
age = 30


def greet():
    print("Hello, World!!!")


print("Names in current scope: ")
print(dir())

print("\nNames in string: ")
print(dir("Hello"))

print("\nNames in math module:")
print(dir(math))
