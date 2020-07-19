# Reviews

def getRating(htmlElement):
    ratingDiv = htmlElement.find(class_="ui_bubble_rating")
    ratingClass = ratingDiv.attrs["class"]
    return int(ratingClass[1][7:9])

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
        da = div.getText().split("wrote a review")
        review["autor"] = da[0]
        review["created"] = da[1]

        div = rev.find(class_="_3J15flPT")
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