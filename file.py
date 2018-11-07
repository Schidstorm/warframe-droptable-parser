import os

def replace(fileName, content):
    if os.path.exists(fileName):
        os.remove(fileName)

    with open(fileName, "w+", "utf-8") as f:
        f.write(content);