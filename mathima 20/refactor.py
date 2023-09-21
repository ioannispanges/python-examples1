from utilities.calculation import add, substract
from utilities.conversion import calsius_to_fah, mile_to_kilometers

result1 = add(5, 3)
result2 = substract(10, 4)

temp = calsius_to_fah(25)
distance = mile_to_kilometers(10)

print("Calculate results:")
print("Add:", result1)
print("Sub", result2)

print("Conversions:")
print("Celsius to Fah:", temp)
print("Miles to Kilo:", distance)
