import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com/Hotel_Review-g1053569-d1112186-Reviews-Zur_Alten_Brucke-Schiltach_Baden_Wurttemberg.html'


def saveJson(filename, dataJson):
    with open('data/'+filename+'.json','w') as outfile:
        json.dump(dataJson, outfile)

def getContent():
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
