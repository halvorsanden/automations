# autofiletimestamper

# auto update timestamps of linked files
# place script and config in project folder
# add file paths in config
# append the script to your build script command:
# && python afts.py

import os
import stat
import time
import re
import ntpath
from aftsconfig import linkedFiles, fetcherFiles

for linkedFile in linkedFiles:
    # creation time in seconds since epoch
    modificTimeEpoch = os.path.getmtime(linkedFile)
    # convert time since epoch to readable format
    creationTime = time.strftime(
        '%Y%m%d%H%M', time.localtime(modificTimeEpoch))
    # remove path from filename
    fileNameFull = ntpath.basename(linkedFile)
    # join filename and creation time
    fileStamp = fileNameFull + "?v=" + creationTime
    # define regexpattern
    fileStampRegex = fileNameFull + r"\?v\=\d+"

    for fetcherFile in fetcherFiles:
        # open/read in file
        with open(fetcherFile, "r", encoding="utf8") as file:
            filedata = file.read()
        # check if there is a match
        searchName = re.search(fileStampRegex, filedata)

        if searchName:
            fileStampOld = searchName.group(0)

            if fileStamp != fileStampOld:
                # replace file stamp string
                filedataChanged = re.sub(fileStampRegex, fileStamp, filedata, flags = re.I)
                # write file again
                with open(fetcherFile, "w", encoding="utf8") as file:
                    file.write(filedataChanged)
                print(fileNameFull + " updated")

            else:
                print(fileNameFull + " not changed")
