from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib

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
    response = request.urlopen(url).read()
    soup= BeautifulSoup(response, "html.parser")
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))

    # convert pdf files to text files while filtering the ones with  ‘discussion’ and ‘homework’ and ‘book’ in the name
    a = "d
