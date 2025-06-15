// autofiletimestamper

// auto update timestamps of linked files
// place script and config in project folder
// add file paths in config
// append the script to your build script command:
// && node afts

import fs from "fs"
import path from "path"
import { linkedFiles, fetcherFiles } from "./aftsconfig.js"

for (const linkedFile of linkedFiles) {
	// creation time object
	const { mtime } = fs.statSync(linkedFile),
		// format time object
		Y = mtime.getFullYear(),
		m = String(mtime.getMonth() + 1).padStart(2, "0"),
		d = mtime.getDate(),
		H = mtime.getHours(),
		M = mtime.getMinutes(),
		creationTime = `${Y}${m}${d}${H}${M}`,
		// remove path from filename
		fileNameFull = path.basename(linkedFile),
		// join filename and creation time
		fileStamp = fileNameFull + "?v=" + creationTime,
		// define regexpattern
		fileStampRegex = new RegExp(fileNameFull + "\\?v\\=\\d+")

	for (const fetcherFile of fetcherFiles) {
		// open/read in file
		fs.readFile(fetcherFile, "utf8", (err, data) => {
			if (err) {
				console.error(err)
				return
			}
			// check if there is a match
			const filedata = data,
				fileStampOld = filedata.match(fileStampRegex)

			if (fileStampOld) {
				if (fileStamp != fileStampOld) {
					// replace file stamp string
					const filedataChanged = filedata.replace(fileStampRegex, fileStamp)
					// write file again
					fs.writeFile(fetcherFile, filedataChanged, (err) => {
						if (err) {
							console.error(err, fileNameFull + " changed but couldn't update")
							return
						}
						console.log("\x1b[33m%s\x1b[0m", fileNameFull + " updated")
					})
				}
			}
		})
	}
}
