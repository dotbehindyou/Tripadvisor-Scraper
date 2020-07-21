import requests
import json
from bs4 import BeautifulSoup

def saveJson(filename, dataJson):
    with open('data/'+filename+'.json','w') as outfile:
        json.dump(dataJson, outfile)

def getContent(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def generateUrl(g, d, or_ = None): # TODO: German, English, etc URL (.de, .com, .fr, etc.)
    result = "https://www.tripadvisor.com/g"+str(g)+"-d"+str(d)

    if or_ != None:
        result = result + "-or" + str(or_)

    return result