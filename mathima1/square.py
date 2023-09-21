def calculate_square_and_cube(number):
    def square(num):
        return num ** 2

    def cube(num):
        return num ** 3

    squared = square(number)
    cubed = cube(number)

    print("Number :", number)
    print("Square: ", squared)
    print("Cube :", cubed)


calculate_square_and_cube(4)
