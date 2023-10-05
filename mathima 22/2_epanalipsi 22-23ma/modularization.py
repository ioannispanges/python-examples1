def calculate_area(radius):
    return 3.14 * radius * radius


def calculate_volume(radius, height):
    return calculate_area(radius) * height


radius = 5
height = 10

area_of_circle = calculate_area(radius)
volume_of_cylinder = calculate_volume(radius, height)

print(f"The area of the circle with radius {radius} is :", area_of_circle)
print(f"The volume of the cylinder with radius {radius} and height {height} is", volume_of_cylinder)
