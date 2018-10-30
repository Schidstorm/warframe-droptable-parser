import urllib.request

cache = {}
def hasCache(name):
    return name in cache
def setCache(name, value):
    cache[name] = value
def getCache(name):
    return cache[name]

def load(url):
    if hasCache(url):
        return getCache(url)
    print('miss ' + url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        setCache(url, html)
        return html
