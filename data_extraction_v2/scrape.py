import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import codecs
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage


# [FILE DESCRIPTION]
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
    for url in url_list:
        url_str = "{}.pdf".format(i) # should think about naming as well. Maybe just store it as numbers for now?
        urlretrieve(url, url_str)
        txt = pdf2txt(url_str)
        pdf_txts.append(txt)
        i = i + 1

    return pdf_txts

#helper to extract text from link of pdf
def pdf2txt(url):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(url, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    i = 1
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        #print(i)
        interpreter.process_page(page)
        i = i + 1

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

webscrape("http://www.google.com")
