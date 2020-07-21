# Tripadvisor-Scraper
Scrap data from a Tripadvisor object (before using it, read the conditions from Tripadvisor)  
[ Not finished yet! ]

## How-To
You need this Python (3) librarys:  
- [json](https://docs.python.org/3/library/json.html)
- [requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

```python
    # Select all reviews from a hotel 
    from Tripadvisor import getContent, saveJson, generateUrl
    from Reviews import getManyReviews

    url = generateUrl(1053569, 1112186)
    soup = getContent(url)
    manyReviews = getManyReviews(soup, 100)
    saveJson('reviews.many.test', manyReviews)
```

## LICENSE
Tripadvisor-Scraper, scrap data from a Tripadvisor object  
Copyright (C) 2020 Christopher Mogler  
  
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.  
  
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.  
  
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.  
