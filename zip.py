import zipfile

def save(zipFileName, dataDict):
    with zipfile.ZipFile(zipFileName, "w") as zipFile:
        for key, data in dataDict.items():
            zipFile.writestr(key, data)