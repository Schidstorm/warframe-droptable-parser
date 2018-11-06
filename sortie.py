from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import httpLoader




def load(url):
    d = pq(httpLoader.load(url))
    missionsTable = d('#sortieRewards + table')
    return parseItemAmountFromItemName( parseMissionRewardTable( missionsTable ) )

def parseMissionRewardTable(pyq):
    missions = []
    currentMissionName = None
    currentRotation = None
    for _line in pyq.find('tr'):
        line = pq(_line)
        if line == None or len(line('.blank-row')) != 0:
            continue
        if len(line('th')) > 0:
            continue
        else:
            itemName = line('td:first').text()
            itemProbabilityText = line('td:last').text()
            probabilitySearch = re.search('[a-zA-Z]+ \((\d+\.\d+)%\)', itemProbabilityText)
            probability = float(probabilitySearch.group(1))
            missions.append({ "item": itemName, "probability": probability / 100})
    return missions

def parseItemAmountFromItemName(missionRewards):
    result = []
    amountReg = '^([0-9]+)[Xx]? (.*)$'
    for reward in missionRewards:
        if re.match(amountReg, reward['item']):
            amountSearch = re.search(amountReg, reward['item'])
            amount = int(amountSearch.group(1))
            item = amountSearch.group(2)
        else:
            amount = 1
            item = reward['item']
        
        newReward = reward.copy()
        newReward['item'] = item
        newReward['amount'] = amount
        result.append(newReward)
    return result

