from data_extraction.webscrape import webscrape
from topic_relationships.keywords import get_keywords

# this program runs the keyword finder script on the scraped pdfs

def build_mapper():
    mapper = {}
    txtfiles, headers = webscrape("http://www.eecs70.org/")
    for i in range(len(txtfiles)):
        with open(txtfiles[i], encoding="utf8") as f:
            text = f.read().replace('\n', '')
            keywords = get_keywords(text)
            mapper[headers[i]] = keywords
    return mapper

global mapper = build_mapper()


if __name__ == "__main__":
    print(build_mapper())
