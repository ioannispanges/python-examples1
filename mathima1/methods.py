def factors(n):
    factors_lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors_lst.append(i)
    return factors_lst


number = 12
print(f"The factors of {number} are: {factors(number)}")
