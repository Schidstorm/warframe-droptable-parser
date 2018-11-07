import os
import codecs

def replace(fileName, content):
    if os.path.exists(fileName):
        os.remove(fileName)

    with codecs.open(fileName, "w+", "utf-8") as f:
        f.write(content);