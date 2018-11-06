import relictChances
import missionRewards
import misscenallousDrops
import modsByItem
import os
import csv
import zip
import file
import datetime

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



print("Writing files to /data/relicts.csv")
file.replace('/data/relicts.csv', csv.stringify(relicts, SEPARATOR))

print("Writing files to /data/missions.csv")
file.replace('/data/missions.csv', csv.stringify(missions, SEPARATOR))

print("Writing files to /data/miscs.csv")
file.replace('/data/miscs.csv', csv.stringify(miscs, SEPARATOR))

print("Writing files to /data/mods.csv")
file.replace('/data/mods.csv', csv.stringify(mods, SEPARATOR))

file.replace('/data/.updateTime', datetime.datetime.now().strftime("%Y-%m-%dT%T%z"))
