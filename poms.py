# playlistmoversorter

# default mode copies the files
# run with parameter -m to move files
# first dialogue asks for playlist
# second dialogue for parent output folder

import os
from tkinter.filedialog import askdirectory, askopenfilename
import ntpath
import re
import shutil
import pathlib

playlist = askopenfilename()
parentPath = askdirectory()

print(playlist)

# set the new folder to the filename part of the playlist path
playlistName = ntpath.basename(playlist)
newFolderName = os.path.splitext(playlistName)[0]

print(newFolderName)

newLocation = parentPath + "\\" + newFolderName

# make directory based on playlist name
if not os.path.exists(newLocation):
    os.makedirs(newLocation)
    print("New folder made: " + newLocation)
else:
    print("Folder already exists: " + newLocation)

# open/read in the playlist
with open(playlist, "r", encoding="utf8") as file:
    dataLines = file.read().splitlines()

trackRegex = r'^[a-zA-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$'
tracks = []

for line in dataLines:
    isTrack = re.match(trackRegex, line)
    if isTrack:
        # add track name to array
        tracks.append(line)

print(tracks)

changedTracks = []
missing = []
for index, line in enumerate(tracks, 1):
    if pathlib.Path(line).exists():
        # get track name from line
        track = ntpath.basename(line)
        # setup new track name and location
        movedTrack = f"{newLocation}\\{index} {track}"
        # rename and move track
        shutil.move(line, movedTrack)
        changedTracks.append(movedTrack)
    else:
        missing.append(line)

print(changedTracks)

# update playlist with movedTrack
# with open(playlist, w, encoding="utf8") as file:
#     file.write(newLocationRegexorsomething)
# for line in dataLines:
# add every filename to the list


# with open(playlist, "w", encoding="utf8") as file:
#     filedataUpdated = file.write()

# number of files missing
missingnum = len(missing)

# number of files sucessfully processed
filenum = len(changedTracks)

print(str(filenum) + " processed")
if missing:
    print(str(missingnum) + " can't be found:")
    print(missing)
else:
    print("No missing files.")
