#Given a directory, find out the file Name having max size recursively 

import os
path=r"C:\Users\N. Sai Swagath\Desktop\java"
max_size=0
max_file=""
for root,dirs,files in os.walk(path):
    for file in files:
        full_path=os.path.join(root,file)
        size=os.path.getsize(full_path)
        
        if size > max_size:
            max_size=size
            max_file=full_path

print(max_file)
print(max_size)