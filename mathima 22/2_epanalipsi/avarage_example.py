def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count


grades = [85, 92, 78, 90, 88]
avarage_grade = calculate_average(grades)
print(avarage_grade)
