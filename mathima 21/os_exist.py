import os

path_to_check = r'C:\\Users\\evdokimos\\Desktop\\untitled3\\mathima 21\\shuffle.py'

if os.path.exists(path_to_check):
    print(f"{path_to_check} exists.")
else:
    print(f"{path_to_check} doesn't exist")
