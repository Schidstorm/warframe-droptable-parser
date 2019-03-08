import os

def replace(fileName, content):
    if os.path.exists(fileName):
        os.remove(fileName)

    write(fileName, content)

def write(fileName, content):
    with open(fileName, "w+") as f:
        f.write(content);