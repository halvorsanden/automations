# autofiletimestamper

import os
import stat
import time
import re
import ntpath
from tkinter.filedialog import askopenfilename

# css or js file
filePath = askopenfilename()  # replace this with something auto later

# Get file creation time of file in seconds since epoch
creationTimesinceEpoc = os.path.getctime(filePath)
# convert time since epoch to readable format
creationTime = time.strftime(
    '%Y%m%d%H%M', time.localtime(creationTimesinceEpoc))
fileNameExtension = ntpath.basename(filePath)
# join only filename and creation time
fileStamp = fileNameExtension + "?v=" + creationTime

print(fileStamp)

# split filepath and extension into two
fileName, fileExtension = os.path.splitext(filePath)
# remove path from filename
fileName = ntpath.basename(fileName)

print(fileName)
print(fileExtension)

searchRegex = fileName + fileExtension + r"\?v\=\d+"

print(searchRegex)

# html file
inPath = askopenfilename()  # replace this with something auto later

# open/read in file
with open(inPath, "r") as file:
    # declare the read file as a variable
    filedata = file.read()

# check if there is something matching the js/css file in the html
searchName = re.search(searchRegex, filedata)

print(searchName)
# the check is currently not working as a stopper
if searchName.group(0):
    fileStampOld = searchName.group(0)
    print(fileStampOld)

    if fileStamp != fileStampOld:

        # Replace string
        filedata_new = re.sub(searchRegex, fileStamp, filedata, flags = re.I)

        # write file again
        with open(inPath, "w") as file:
            file.write(filedata_new)

        print(fileName + fileExtension + " updated")

    else:
        print("Nothing to update")
