def sum_squares(numbers):
    even_numbers = [x for x in numbers if x % 2 == 0]
    squared_numbers = [x ** 2 for x in even_numbers]
    return sum(squared_numbers)


numbers = [1, 2, 3, 4, 5, 6]
result = sum_squares(numbers)
print(result)
