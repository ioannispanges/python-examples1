def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


number = 12
factor_gen = factors(number)
print(f"The factors of {number} are :{list(factor_gen)}")
