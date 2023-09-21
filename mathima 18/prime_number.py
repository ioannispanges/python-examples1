import math


def prime_sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def main():
    n = int(input("Enter a number: "))
    primes = prime_sieve(n)
    print("The primes number less than or equal to", n, "are:")
    for p in primes:
        print(p)


if __name__ == "__main__":
    main()
