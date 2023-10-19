try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
else:
    print("File open successfully")
    file.close()

