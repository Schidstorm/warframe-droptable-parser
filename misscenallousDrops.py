from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import httpLoader




def load(url):
    d = pq(httpLoader.load(url))
    miscTable = d('#miscItems + table')
    return parseEnemyDropsTable(miscTable)

def parseEnemyDropsTable(pyq):
    enemies = []
    currentEnemyName = None
    currentDropChance = None
    for _line in pyq.find('tr'):
        line = pq(_line)
        if line == None or len(line('.blank-row')) != 0:
            continue
        if len(line('th')) > 0:
            currentEnemyName = line('th:first').text()
            dropChanceText = line('th:last').text()
            dropChanceSearch = re.search('Miscellaneous Drop Chance: (\d+\.\d+)%', dropChanceText)
            currentDropChance = float(dropChanceSearch.group(1))
        else:
            itemName = line('td').eq(1).text()
            itemProbabilityText = line('td:last').text()
            probabilitySearch = re.search('[a-zA-Z]+ \((\d+\.\d+)%\)', itemProbabilityText)
            probability = float(probabilitySearch.group(1))
            enemies.append({ "enemy": currentEnemyName, "dropChance": currentDropChance, "itemName": itemName, "probability": probability / 100})
    return enemies
