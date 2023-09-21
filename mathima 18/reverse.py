def reverse(number):
    rev = 0
    number, mod = number // 10, number % 10
    while number > 0:
        print(rev, mod, number)
        rev = 10 * rev + mod
        number, mod = number // 10, number % 10
        print(rev, mod, number)
    rev = 10 * rev + mod
    return rev


mypi = 3.14

num_to_reverse = 12345
reversed_num = reverse(num_to_reverse)
print("Reversed number:", reversed_num)

print("Value of mypi", mypi)


if __name__ == "__main__":
    print("Einai ok")
