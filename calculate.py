def calculate_average(numbers):
    # 1simeio kalesmatos to sum apotelesma 75
    total = sum(numbers)
    # 2simeio kalesmato einai to average 75  / 5 = 15
    avarage1 = total / len(numbers)
    avarage2 = total + len(numbers)
    avarage3 = total - len(numbers)
    avarage4 = total * len(numbers)

    # 3 simeio epistrofi timis avarage
    return avarage1, avarage2, avarage3, avarage4


# kalesma sunartisis

numbers_list = [5, 10, 15, 20, 25]
result = calculate_average(numbers_list)
print("The average is: ", result)
