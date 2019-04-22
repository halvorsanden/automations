import os

path = 'd:\\test\\'

files = []  # defines list, empty
ignored = 'Thumbs.db'
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(file)  # adds every filename (f) to the list

filesclean = files[:]
filesclean.remove(ignored)

letters = []  # new list
for f in filesclean:  # for every filename
    letters.append(f[:1])  # add the first letter to the new list

letters = list(dict.fromkeys(letters))  # removes duplicates from new list

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

# make sets with comparisons
missing = set(alphabet).difference(letters)
extra = set(letters).difference(alphabet)
# convert them to lists - just because
missing = list(missing)
extra = list(extra)

if missing:
    print("There's room for:")
    print(missing)
else:
    print("All letters are in use.")

if extra:
    print("Extra prefixes used:")
    print(extra)
else:
    print("No extra prefixes in use.")
