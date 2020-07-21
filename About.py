# About
from Tripadvisor import getContent, saveJson, generateUrl
from Reviews import getRating


def getAbout(soup):
    result = {
        "id": None,
        "ratingAverage": None,
        "ratingCount": None,
        "subRating":{
            "location": None,
            "cleanliness": None,
            "service": None,
            "value": None,
        },
        "isTravelersChoice": False,
        "roomFeauters": [],
        "amenities": [],
        "roomTypes": [],
        "languages": [],
        "hotelClass": None,
        "hotelStyle": [],
        "description": None,
    }

    about = soup.find(class_="_3koVEFzz")   

    div = about.find(class_='_3cjYfwwQ')
    ave = div.getText().replace(".", "").replace(",", "")
    result["ratingAverage"] = int(ave)

    div = about.find(class_='_3jEYFo-z')
    ave = div.getText().replace(" reviews", "")
    result["ratingCount"] = int(ave)
    
    divs = about.find_all(class_='_1krg1t5y')
    for subRating in divs:
        t = subRating.getText()
        result["subRating"][t.lower()] = getRating(subRating)

    div = about.find(class_="GzEo7hAU")
    if len(div.getText()) > 0:
        result["isTravelersChoice"] = True
    
    div = about.find(class_="cPQsENeY")
    result["description"] = div.getText()

    props = about.find_all(class_="_1mJdgpMJ")
    for prop in props:
        sib = prop.nextSibling.find_all(class_="_2rdvbNSg")
        if prop.getText() == "Property amenities":
            for amenities in sib:
                result["amenities"].append(amenities.getText())
        elif prop.getText() == "Room features":
            for roomFeauters in sib:
                result["roomFeauters"].append(roomFeauters.getText())
        elif prop.getText() == "Room types":
            for roomTypes in sib:
                result["roomTypes"].append(roomTypes.getText())

    return result

def testAbout():
    url = generateUrl(1053569, 1112186)
    soup = getContent(url)
    saveJson('about.test', getAbout(soup))

if __name__ == "__main__":
    testAbout()