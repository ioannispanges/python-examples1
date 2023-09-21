def hanoi(n, source, aux, dest):
    if n == 1:
        print("Move disk 1 from", source, "to", dest)
    else:
        hanoi(n - 1, source, dest, aux)
        print("Move disk", n, "from", source, "to", dest)
        hanoi(n - 1, aux, source, dest)


def main():
    n = int(input("Enter the number of disks: "))
    hanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()
