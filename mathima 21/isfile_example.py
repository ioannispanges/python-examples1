import os

path_to_check = "../mathima 21/os_exist.py"

if os.path.isfile(path_to_check):
    print(f"{path_to_check} is a file.")
else:
    print(f"{path_to_check} is not a file")
