# autofiletimestamper

import os
import stat
import time
import re
import ntpath
from aftsconfig import linkedFiles, fetcherFiles

for linkedFile in linkedFiles:
    # creation time in seconds since epoch
    creationTimeEpoch = os.path.getctime(linkedFile)
    # convert time since epoch to readable format
    creationTime = time.strftime(
        '%Y%m%d%H%M', time.localtime(creationTimeEpoch))
    # remove path from filename
    fileNameFull = ntpath.basename(linkedFile)
    # join filename and creation time
    fileStamp = fileNameFull + "?v=" + creationTime
    # define regexpattern
    fileStampRegex = fileNameFull + r"\?v\=\d+"

    # html file
    fetcherFile = fetcherFiles[0]
    # open/read in file
    with open(fetcherFile, "r") as file:
        filedata = file.read()
    # check if there is a match
    searchName = re.search(fileStampRegex, filedata)

    fileStampOld = searchName.group(0)

    if fileStamp != fileStampOld:
        # Replace string
        filedataChanged = re.sub(fileStampRegex, fileStamp, filedata, flags = re.I)
        # write file again
        with open(fetcherFile, "w") as file:
            file.write(filedataChanged)
        print(fileNameFull + " updated")

    else:
        print(fileNameFull + " not changed")
