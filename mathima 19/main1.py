import generator_password


def main1():
    print("Random Password Generator")
    print("-------------------------")

    length = int(input("Enter the desired length of the password: "))
    password = generator_password.generate_password(length)

    print(f"Generated Password {password}")


if __name__ == "__main__":
    main1()
