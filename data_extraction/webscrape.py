import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from urllib.request import urlretrieve

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# # checpoint
# import sys
# import logging
# import six
# import pdfminer.settings
# pdfminer.settings.STRICT = False
# import pdfminer.high_level
# import pdfminer.layout

# python file for scraping websites
# Input: URLs
# Output: JSON files in format of d3 API

# ## use google cloud API to extract data and create relations among subtopics of exctracted data
#
# Within each website, possible formats for where content is stored is
# 1) PDFs (lecture notes, textbooks)
# 2) Google Slides "....docs.google.com"
# 3) HTML / online textbooks ".....html" files
#
# when extracting these three types of data, we look for certain keywords such as
# "lecture", "schedule", "notes", etc.
#
#
# Possible problems:
# 1) Extracted keywords aren't really relevant to the actual material
# -> Autism example in data 100, might catch autism as a keyword
# -> We need to figure out a way to remove these words from our output file


def webscrape(url):
    # connect to website and get list of all pdfs
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a[href$='.pdf']")

    # clean the pdf link names
    url_list = []
    for el in links:
        if(el['href'].startswith('http')):
            url_list.append(el['href'])
        else:
            url_list.append(url + el['href'])

    # filter pdfs that have the words ‘discussion’ and ‘homework’ and ‘book’ in the title
    # filtered_urls = [el for el in url_list if 'discussion' not in el and 'homework' not in el and 'book' not in el]
    filtered_urls = []
    for el in url_list:
        if 'discussion' not in el and 'homework' not in el and 'book' not in el and el not in filtered_urls:
            filtered_urls.append(el)

    # filtered_urls now contains the urls of pdfs that aren't homeworks, discussions, or books without any duplicates
    for el in filtered_urls:
        print(el)

    # example = filtered_urls[4]
    # urlretrieve(example, "note4.pdf")
    # print(pdf2txt("note4.pdf"))

    pdf_txts = []
    i = 0
    for url in filtered_urls:
        url_str = "{}.pdf".format(i)
        urlretrieve(url, url_str)
        pdf_txts.append(pdf2txt(url_str))
        i = i + 1

    print(pdf_txts[10])

    # for url in filtered_urls[0:3]:
    #     url_str = "{}.pdf".format(i)
    #     urlretrieve(url, url_str)
    #     pdf_txts.append(pdf2txt(url_str))
    #     i = i + 1
    # print(pdf_txts[2])
    # for url in filtered_urls[4:]:
    #     url_str = "{}.pdf".format(i)
    #     urlretrieve(url, url_str)
    #     pdf_txts.append(pdf2txt(url_str))
    #     i = i + 1

    # url = filtered_urls[5]
    # url_str = "5.pdf"
    # urlretrieve(url, url_str)
    #
    # pdf_txts.append(pdf2txt(url_str))
    #
    # print(pdf_txts[0])

    # example_url = filtered_urls[0]
    # print(example_url)
    #
    # urlretrieve(example_url, "a.pdf")
    # txt = pdf2txt("a.pdf")
    # print(txt)

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
        print(i)
        interpreter.process_page(page)
        i = i +1

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

# def extract_text(files=[], outfile='-',
#             _py2_no_more_posargs=None,  # Bloody Python2 needs a shim
#             no_laparams=False, all_texts=None, detect_vertical=None, # LAParams
#             word_margin=None, char_margin=None, line_margin=None, boxes_flow=None, # LAParams
#             output_type='text', codec='utf-8', strip_control=False,
#             maxpages=0, page_numbers=None, password="", scale=1.0, rotation=0,
#             layoutmode='normal', output_dir=None, debug=False,
#             disable_caching=False, **other):
#     if _py2_no_more_posargs is not None:
#         raise ValueError("Too many positional arguments passed.")
#     if not files:
#         raise ValueError("Must provide files to work upon!")
#
#     # If any LAParams group arguments were passed, create an LAParams object and
#     # populate with given args. Otherwise, set it to None.
#     if not no_laparams:
#         laparams = pdfminer.layout.LAParams()
#         for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
#             paramv = locals().get(param, None)
#             if paramv is not None:
#                 setattr(laparams, param, paramv)
#     else:
#         laparams = None
#
#     imagewriter = None
#     if output_dir:
#         imagewriter = ImageWriter(output_dir)
#
#     if output_type == "text" and outfile != "-":
#         for override, alttype in (  (".htm", "html"),
#                                     (".html", "html"),
#                                     (".xml", "xml"),
#                                     (".tag", "tag") ):
#             if outfile.endswith(override):
#                 output_type = alttype
#
#     if outfile == "-":
#         outfp = sys.stdout
#         if outfp.encoding is not None:
#             codec = 'utf-8'
#     else:
#         outfp = open(outfile, "wb")
#
#
#     for fname in files:
#         with open(fname, "rb") as fp:
#             pdfminer.high_level.extract_text_to_fp(fp, **locals())
#     return outfp

webscrape("http://www.eecs70.org/")
