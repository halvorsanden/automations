# playlistmoversorter

# no dry runs at the moment, be sure to have backups
# first dialogue asks for playlist
# second dialogue for parent output folder

import os
from tkinter.filedialog import askdirectory, askopenfilename
import ntpath
import re
import shutil
from pathlib import Path

playlist = askopenfilename()
parentPath = askdirectory()
playlistName = ntpath.basename(playlist)
newFolderName = os.path.splitext(playlistName)[0]
newLocation = f"{parentPath}\\{newFolderName}"

if not os.path.exists(newLocation):
    os.makedirs(newLocation)
    print(f"New folder made: {newLocation}")
else:
    print(f"Folder already exists: {newLocation}")

with open(playlist, "r", encoding="utf8") as file:
    originLines = file.read().splitlines()

trackRegex = r'^[a-zA-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$'
tracks = []

for line in originLines:
    isTrack = re.match(trackRegex, line)
    if isTrack:
        # add track name to array
        tracks.append(line)

changedTracks = []
missing = []
for index, line in enumerate(tracks, 1):
    if Path(line).exists():
        # get track name from line
        track = ntpath.basename(line)
        # change index to string and add leading zeros
        trackNum = f"{index}".zfill(3)
        # setup new track name and location
        movedTrack = Path(f"{newLocation}/{trackNum} {track}")
        print(movedTrack)
        # rename and move track
        shutil.move(line, movedTrack)
        changedTracks.append(movedTrack)
    else:
        missing.append(line)

for lineIndex, line in enumerate(originLines):
    isTrack = re.match(trackRegex, line)
    if isTrack:
        # get the filename from that line
        originTrack = ntpath.basename(line)
        for newLine in changedTracks:
            newTrack = ntpath.basename(newLine).split(maxsplit=1)
            cleanNewTrack = newTrack[1]
            # run new filename against the filename of the original file
            if originTrack == cleanNewTrack:
                # remove original line at lineIndex
                originLines.remove(line)
                # insert newLine at lineIndex
                originLines.insert(lineIndex, f"{newLine}")

# update playlist with new line content and empty last line
with open(playlist, "w", encoding="utf8") as file:
    file.write("\n".join(originLines) + "\n")

missingnum = len(missing)
filenum = len(changedTracks)

print(f"{filenum} processed")
if missing:
    print(f"{missingnum} can't be found:")
    print(missing)
else:
    print("No missing files.")
