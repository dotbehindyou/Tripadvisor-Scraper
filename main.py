import requests
import json
import Reviews
import About
from bs4 import BeautifulSoup

url = ''
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

reviews = Reviews.getReviews(soup)   
with open('data/reviews.json', 'w') as outfile:
    json.dump(reviews, outfile)

about = About.getAbout(soup)
with open('data/about.json', 'w') as outfile:
    json.dump(about, outfile)


print("Done.")