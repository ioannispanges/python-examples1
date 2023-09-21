import geometry


def main():
    print("Geometry Calculator")
    print("1. Calculate Circle Area")
    print("2. Calculate Rectangle Area")
    print("3. Calculate Triangle Area")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = geometry.calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    elif choice == 2:
        width = float(input("Enter the width of the rectangle :"))
        height = float(input("Enter the height of the rectangle"))
        area = geometry.calculate_rectangle_area(width, height)
        print(f"The area of rectangle with width {width} and height {height} is {area:.2f}")
    elif choice == 3:
        base = float(input("Enter the base of the triangleW"))
        height = float(input("Enter the height of the triangle: "))
        area = geometry.calculate_triangle_area(base, height)
        print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
