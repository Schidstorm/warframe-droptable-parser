import relictChances
import missionRewards
import misscenallousDrops
import modsByItem
import dynamicRewards
import sortie
import os
import csv
import zip
import file
import datetime

DROPTABLE_URL = 'http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html'
SEPARATOR = ";"
ZIP_FILE_NAME = "data.zip"

parsers = {
    'relicts': relictChances,
    'missions': missionRewards,
    'miscs': misscenallousDrops,
    'mods': modsByItem,
    'dynamic': dynamicRewards,
    'sortie': sortie
}

def saveDataFile(dataName, content):
    file.replace('/data/' + dataName + "_en.csv", csv.stringify(content, SEPARATOR))
    file.replace('/data/' + dataName + "_de.csv", csv.stringify(content, SEPARATOR).replace('.', ','))

print("Create Data Directory")
if not os.path.exists("data"):
    os.mkdir("data")

for key, value in parsers.items():
    print("Loading " + key)
    content = value.load(DROPTABLE_URL)
    print("Writing files to /data/"+key+".csv")
    saveDataFile(key, content)

file.replace('/data/.updateTime', datetime.datetime.now().strftime("%Y-%m-%dT%T%z"))
