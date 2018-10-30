from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import httpLoader




def load(url):
    d = pq(httpLoader.load(url))
    relictsTable = d('#relicRewards + table')
    return parseRelictsTable(relictsTable)

def parseRelictsTable(pyq):
    relicts = []
    currentRelictName = None
    for _line in pyq.find('tr'):
        line = pq(_line)
        if line == None or len(line('.blank-row')) != 0:
            continue
        if len(line('th')) > 0:
            currentRelictName = line('th').text()
        else:
            if currentRelictName != None:
                itemName = line('td:first').text()
                itemProbabilityText = line('td:last').text()
                probabilitySearch = re.search('[a-zA-Z]+ \((\d+\.\d+)%\)', itemProbabilityText)
                probability = float(probabilitySearch.group(1))
                relicts.append({ "relict": currentRelictName, "item": itemName, "probability": probability / 100})
    return relicts
