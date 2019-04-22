import os

path = 'd:\\test\\'

files = []  # defines list, empty
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(file)  # adds every filename (f) to the list

letters = []  # new list
for f in files:  # for every filename
    letters.append(f[:1])  # add the first letter to the new list

letters = list(dict.fromkeys(letters))  # removes duplicates from new list
print(letters)
