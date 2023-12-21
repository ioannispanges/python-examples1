import os
import shutil
import time
current_file = r'C:\Users\evdokimos\Desktop\python\mathima 33\services\price.xls'
new_file = r'C:\Users\evdokimos\Desktop\python\mathima 33\latest\price.xls'

attr_current = os.stat(current_file)
attr_new = os.stat(new_file)

print(f"Modification time of current file: {time.ctime(attr_current.st_mtime)}")
print(f'Modification time of new file:{time.ctime(attr_new.st_mtime)}')

if attr_current.st_mtime < attr_new.st_mtime:
    shutil.copy(new_file, current_file)

    print(f"{new_file} has been compied to {current_file} due to its more recent modification time")
else:
    print("No action was take as the modification time of the new file")