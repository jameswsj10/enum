import os
import requests
import regex as re
from bs4 import BeautifulSoup

def getWikipediaPage(keyword):
    words = keyword.split()
    concat = "+".join(words)
    url = 'https://en.wikipedia.org/w/index.php?search=' + concat + '&title=Special:Search&go=Go&ns0=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.html.body.find_all('a', attrs={'href': re.compile("^/wiki/")})
    return 'en.wikipedia.org' + links[2].get('href')


# def searchWikiPage(url, keyword):
#   1. make request to get the HTML content from the url
#   2. iterate through h2 tags (these are the main topic headings)
#   3. get the text under each h2 tag. if there are any subheadings (h3 tags),
#      iterate through those as well and search the text for a keyword match.
#      We will have to perform stemming/lemmatization as necessary.
#   Data Structure: list of headers
#   Return the headers relevant to the keyword
#   (ignore See Also and after)



# We probably don't need this
# def getTableofContentsTags(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     all_tags = soup.find_all('h2')[1:-5]
#     for elem in all_tags:
#         print(elem.contents[0].contents[0])



if __name__ == '__main__':
    getWikipediaPage('Inheritance Computer Science')
    # getTableofContentsTags('https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)')
