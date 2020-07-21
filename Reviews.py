# Reviews
from Tripadvisor import getContent, saveJson, generateUrl
import requests

def getRating(htmlElement):
    ratingDiv = htmlElement.find(class_="ui_bubble_rating")
    if ratingDiv != None:
        ratingClass = ratingDiv.attrs["class"]
        return int(ratingClass[1][7:9])
    return 0

def getReviews(soup): # TODO: Alle Reviews laden: (URL: Reviews-or10)
    result = []
    revs = soup.find_all(class_="_2wrUUKlw")
    for rev in revs:
        review = {
            "header": None,
            "body": None,
            "autor": None,
            "created": None,
            "place": None,
            "roomsRating": None,
            "serviceRating": None,
            "locationRating": None
        }
        div = rev.find(class_="ocfR3SKN")
        review["header"] = div.getText()

        div = rev.find(class_="IRsGHoPm")
        review["body"] = div.getText()

        div = rev.find(class_="_2fxQ4TOx")
        if div != None:
            da = div.getText().split("wrote a review")
            review["autor"] = da[0]
            review["created"] = da[1]

        div = rev.find(class_="_3J15flPT")
        if div != None:
            review["place"] = div.getText()

        divs = rev.find_all(class_="_3ErKuh24 _1OrVnQ-J")
        for ratingItem in divs:
            rtStr = ratingItem.getText()
            if rtStr.find("Rooms") > -1:
                review["roomsRating"] = getRating(ratingItem)
            elif rtStr.find("Service") > -1:
                review["serviceRating"] = getRating(ratingItem)
            elif rtStr.find("Location") > -1:
                review["locationRating"] = getRating(ratingItem)
        
        result.append(review)

    return result

def getManyReviews(soup, count = None):
    revPageList = soup.find(class_="_16gKMTFp")
    revPages = revPageList.find_all('a', class_="pageNum")

    lastPageBtn = revPages[len(revPages) -1 ]
    href = lastPageBtn.attrs["href"]

    startUrl = href.find("-or") + 3
    endUrl = href.find("-", startUrl)
    lastPageNr = int(href[startUrl:endUrl])

    if count == None or lastPageNr < count:
        count = lastPageNr

    urlTemplate = href.replace(href[startUrl:endUrl], "{x}")

    result = []

    for or_ in range(5, count, 5):
        subUrl = 'https://www.tripadvisor.com/' + urlTemplate.replace("{x}", str(or_))
        subSoup = getContent(subUrl)
        result.extend(getReviews(subSoup))

    return result

def testReviews():
    url = generateUrl(1053569, 1112186)
    soup = getContent(url)
    manyReviews = getManyReviews(soup, 100)
    saveJson('reviews.many.test', manyReviews)

if __name__ == "__main__":
    testReviews()