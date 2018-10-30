import relictChances
import missionRewards
import misscenallousDrops
import modsByItem
import os
import csv
import zip

DROPTABLE_URL = 'http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html'
SEPARATOR = ";"
ZIP_FILE_NAME = "data.zip"


print("Loding Relicts")
relicts = relictChances.load(DROPTABLE_URL)

print("Loading Mission")
missions = missionRewards.load(DROPTABLE_URL)

print("Loading Misc Drops")
miscs = misscenallousDrops.load(DROPTABLE_URL)

print("Loading Mod Drops")
mods = modsByItem.load(DROPTABLE_URL)

print("Create Data Directory")
if not os.path.exists("data"):
    os.mkdir("data")



print("Writing Zip to " + ZIP_FILE_NAME)
zip.save("data/" + ZIP_FILE_NAME, {
    "relicts.csv": csv.stringify(relicts, SEPARATOR),
    "mission.csv": csv.stringify(missions, SEPARATOR),
    "miscs.csv": csv.stringify(miscs, SEPARATOR),
    "mods.csv": csv.stringify(mods, SEPARATOR)
})
