import os

path = 'd:\\test\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
         files.append(file)

for f in files:
    print(f)