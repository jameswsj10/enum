import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import codecs
from io import StringIO

# python file for scraping websites
# Input: URL
# Output: array of txts of the pdfs we scrape the url

# Within each website, possible formats for where content is stored is
# 1) PDFs (lecture notes, textbooks)
# 2) Google Slides "....docs.google.com"
# 3) HTML / online textbooks ".....html" files
def webscrape(url):
    """ Grabs all the pdf files in a website and converts them into text files, storing them in an array that preserves
    order.

    Inputs: website url
    Output: array of text <- CAN BE CHANGED CORRESPONDINGLY

    """
    # connect to website and get list of all pdfs
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a[href$='.pdf']")

    # clean the pdf link names
    url_list = []
    for el in links:
        if el['href'].startswith('http'):
            url_list.append(el['href'])
        else:
            url_list.append(url + el['href'])

    # TODO: have to change the pdf to text conversion here. (add the pdf2txt function)
    # TO RITVIK: i had it so that we add in the text itself, but we can have it so that it appends the txt file
    pdf_txts = []
    i = 0
    for url in filtered_urls:
        url_str = "{}.pdf".format(i) # should think about naming as well. Maybe just store it as numbers for now?
        urlretrieve(url, url_str)
        txt = pdf2txt(url_str)
        pdf_txts.append(txt)
        i = i + 1

    return pdf_txts
