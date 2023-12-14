import os

file_path = 'C:\\Users\\evdokimos\\Desktop\\python\\john.py'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been successfully removed")
else:
    print(f"The file{file_path}does not exist")
# if not Exception:
#     os.remove(file_path)
#     print(f"The file{file_path} has been successfully removed")
# else:
#     print(f"The file {file_path} does not exist")
