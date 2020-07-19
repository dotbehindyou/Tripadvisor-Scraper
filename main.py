import Reviews
import About
from Tripadvisor import saveJson, getContent

import json

def run_reviews(soup):
    reviews = Reviews.getReviews(soup)
    saveJson('reviews',reviews)

def run_about(soup):
    about = About.getAbout(soup)
    saveJson('about',about)

if __name__ == "__main__":
    soup = getContent()
    run_reviews(soup)
    run_about(soup)
    print("Done.")