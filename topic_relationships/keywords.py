from google.cloud import language
import os
import argparse
import pandas as pd
from textblob import TextBlob
import nltk
#nltk.download('words')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + r"\private-key.json"

def get_keywords(text):
    client = language.LanguageServiceClient()
    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    ent_analysis = client.analyze_entities(document, encoding_type= 'UTF8')
    entities = ent_analysis.entities
    data = {'word': [], 'score': []}
    salience = pd.DataFrame(data)
    all_names = []
    all_scores = []
    for entity in entities:
        all_names.append(entity.name)
        all_scores.append(entity.salience)
    salience['word'] = all_names
    salience['score'] = all_scores
    top_k = salience.sort_values('score', ascending=False)
    top_100 = top_k[top_k['word'].str.len() >= 3].iloc[0:100]
    strs = "".join([str(x) + " " for x in top_100['word'].str.replace(r'[\d]', " ")][0:100])
    blob = TextBlob(strs)
    words = set(nltk.corpus.words.words('en'))

    def isname1(string):
        return any([w not in words for w in string.lower().split()])

    def contains_duplicates(string):
        setted = set(string.split())
        splitted = string.split()
        if len(setted) < len(splitted):
            return True
        return False

    keywords = []
    for word in blob.noun_phrases:
        if not isname1(word) and not word.count(' ') > 1 and len(word) <= 20 and not contains_duplicates(word):
            keywords.append(word)
    print(list(set(keywords)))
    return list(set(keywords))

# filter text to remove all words in trivial topic word banks
# filter text to remove all duplicates
# strs = str.split()
# str = (" ".join(sorted(set(strs), key=strs.index)))



#def filter


# def text_to_json_request(text):
#     data = {"document": {
#         "type": "PLAIN_TEXT",
#         "content": text},
#         "encodingType": "UTF"
#     }
#     name = 'data.txt'
#     with open(name, 'w') as outfile:
#         json.dump(data, outfile)
#     return name

# test if our keyword function works
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'textfile_name',
        help='The filename of the text file you\'d like to analyze.')
    args = parser.parse_args()
    with open(args.textfile_name, encoding="utf8") as file:
        text = file.read().replace('\n', '')
    get_keywords(text)