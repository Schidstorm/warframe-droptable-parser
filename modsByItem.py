from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import httpLoader




def load(url):
    d = pq(httpLoader.load(url))
    miscTable = d('#modLocations + table')
    return parseModLocationsTable(miscTable)

def parseModLocationsTable(pyq):
    modDrops = []
    currentMod = None
    for _line in pyq.find('tr'):
        line = pq(_line)
        if line == None or len(line('.blank-row')) != 0 or len(line('th')) > 1:
            continue
        if len(line('th')) == 1:
            currentMod = line('th').text()
        else:
            enemyName = line('td').eq(0).text()
            dropChanceSearch = re.search('(\d+\.\d+)%', line('td').eq(1).text())
            dropChance = float(dropChanceSearch.group(1))
            chanceSearch = re.search('[a-zA-Z]+ \((\d+\.\d+)%\)', line('td:last').text())
            chance = float(chanceSearch.group(1))
            modDrops.append({ "mod": currentMod, "enemy": enemyName, "dropChance": dropChance / 100, "chance": chance / 100})
    return modDrops
