import os
import requests
import regex as re
from bs4 import BeautifulSoup, NavigableString, Tag

# importing libraries necessary to stem and lemmatize word
import nltk
# nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()

# function seems to be giving back inconsistent results for some keywords like 'Particles Chemistry' (2 diff results)
def getWikipediaPage(keyword):
    """Returns wikipedia page of given keyword

    >>> getWikipediaPage('Inheritance Computer Science')
    en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)
    >>> getWikipediaPage('Particles Chemistry')
    en.wikipedia.org/wiki/Particle

    """
    concat = keyword.replace(' ', '+')
    url = 'https://en.wikipedia.org/w/index.php?search={}&title=Special:Search&go=Go&ns0=1'.format(concat)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.html.body.find_all('a', attrs={'href': re.compile("^/wiki/")})
    return 'en.wikipedia.org{}'.format(links[2].get('href'))    #.format is the faster than adding strings


# def searchWikiPage(url, keyword):
#   1. make request to get the HTML content from the url
#   2. iterate through h2 tags (these are the main topic headings)
#   3. get the text under each h2 tag. if there are any subheadings (h3 tags),
#      iterate through those as well and search the text for a keyword match.
#      We will have to perform stemming/lemmatization as necessary.
#   Data Structure: list of headers
#   Return the headers relevant to the keyword
#   (ignore See Also and after)

def findRelevantHeadings(url, keyword):
    """In one pass of the wikipedia page, return all headings and subheadings
    of the page with a match to the keyword in the text

    >>> findRelevantHeadings(url, keyword)
    ["[h2]/[h3]", "[h2]"]
    >>> findRelevantHeadings("http://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)", "polymorph")
    ["Applications/Code reuse", "Design Constraints"]

    ^ change output as needed (maybe a linked list)
    """
    headings = []
    keyword_porter = porter.stem(keyword)       # two different ways of stemming and lemmatizing, we should search both
    keyword_lancaster = lancaster.stem(keyword)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    h2 = ""
    h3 = ""

    for header in soup.find_all('h2')[1:-5]:
        nextNode = header
        h2 = header
        h3 = ""
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == "h2":
                    break
                if nextNode.name == "h3":
                    h3 = nextNode.get_text(strip=True).strip()[:-6]
                #search through following information to find if keyword exists in given text
                if (nextNode.get_text(strip=True).strip().find(keyword) != -1): # LETS SEE IF WE SHOULD USE PORTER OR LANC
                    #if keyword in information, add to list
                    if h3 == "":
                        headings.append(h2.text[:-6])
                    else:
                        headings.append(h2.text[:-6] + "/" + h3)
                    break
    # print(headings)
    return headings

# We probably don't need this
# def getTableofContentsTags(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     all_tags = soup.find_all('h2')[1:-5]
#     for elem in all_tags:
#         print(elem.contents[0].contents[0])

if __name__ == '__main__':
    #getWikipediaPage('Particles Chemistry')
    findRelevantHeadings("http://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)", "polymorph")
    # getTableofContentsTags('https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)')
