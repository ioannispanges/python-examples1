import os

path_to_check = "../mathima 21/"

if os.path.isdir(path_to_check):
    print(f"{path_to_check} is a directory.")
else:
    print(f"{path_to_check} is a not directory")
