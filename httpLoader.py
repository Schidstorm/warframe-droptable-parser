import urllib.request
import urllib2

def _loadWithoutCache(url):
    req = urllib2.Request(url)
    req.add_header('From', 'dominik@schidlowski.eu')
    req.add_header('User-Agent', 'warframe-droptable-parser')
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content

cache = {}
def _hasCache(name):
    return name in cache
def _setCache(name, value):
    cache[name] = value
def _getCache(name):
    return cache[name]

def load(url):
    if _hasCache(url):
        return _getCache(url)
    print('miss ' + url)
    html = _loadWithoutCache(url)
    _setCache(url, html)
    return html

