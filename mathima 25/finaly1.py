file = None
try:
    file = open("example.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("Error: File not found")
finally:
    if file is not None:
        file.close()
        print("File closed.")

