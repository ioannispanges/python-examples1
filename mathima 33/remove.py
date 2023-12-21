import os
import contextlib

#
file_path = 'C:\\Users\\evdokimos\\Desktop\\python\\john.py'
#
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"The file {file_path} has been successfully removed")
# else:
#     print(f"The file{file_path}does not exist")
try:
    os.remove(file_path)
    print(f"The file{file_path} has been successfully removed")
except FileNotFoundError:
    print(f"The file {file_path} does not exist")
