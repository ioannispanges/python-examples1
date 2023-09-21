def greet():
    print("submodule")


print("Submodule is being imported.__name__=", __name__)

if __name__ == "__main__":
    print("Run the program")
    print(greet())
