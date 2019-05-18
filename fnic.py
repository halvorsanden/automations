# filenameindexchecker

import os
from tkinter.filedialog import askdirectory
from fnicconfig import alphabet

path = askdirectory()

files = []
ignored = 'Thumbs.db'
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        # add every filename (f) to the list
        files.append(file)

filesclean = files[:]
if ignored in filesclean:
    filesclean.remove(ignored)

letters = []
for f in filesclean:
    # add the first letter to the new list
    letters.append(f[:1])

# remove duplicates from new list
letters = list(dict.fromkeys(letters))

# make sets with comparisons
missing = set(alphabet).difference(letters)
extra = set(letters).difference(alphabet)
# convert sets to lists
missing = list(missing)
extra = list(extra)

print(path)
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
