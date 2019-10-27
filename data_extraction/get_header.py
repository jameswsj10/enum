from google.cloud import language
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Users/jungwonsuk/Calhacks6/data_extraction/private-key.json"
import argparse
import pandas as pd

def get_header(text):
    text = text[100:250]
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
    top_k = top_k[top_k['word'].str.len() >= 3]
    header = top_k['word'].iloc[0]

    headerwords = header.split()
    header = []
    for word in headerwords:
        # if "Intro" in word:
        #     break
        if ":" in word:
            word = word[:len(word)-1]
            header.append(word)
            break
        header.append(word)
    result_header = " ".join(header)
    # print(result_header)
    return result_header
    # # filter the numbers from the texts
    # text_to_filter = pdf_txts[4]
    # str = re.sub(r'[\d]', " ", text_to_filter)

# get_header('CS 70 Discrete Mathematics and Probability Theory Fall 2019 Alistair Sinclair and Yun Song Note 5 1 Graph Theory: An Introduction One of the fundamental ideas in computer science is the notion of abstraction: capturing the essence or the core of some complex situation by a simple model. Some of the largest and most complex entities we might deal wi')

# a = "CS 70 Fall 2019 Discrete Mathematics and Probability Theory Alistair Sinclair and Yun Song Note 3 1 Mathematical Induction Introduction. In this note, we introduce the proof technique of mathematical induction. Induction is a powerful tool which is used to establish that a statement holds for all natural numbers. Of course, there are inﬁnitely many natural numbers — induction provides a way to reason about them by ﬁnite means."
# get_header(a)

b = "CS 70 Discrete Mathematics and Probability Theory Fall 2019 Alistair Sinclair and Yun Song Note 5 1Conditional Probability, Independence, and Combinations of Events"
get_header(b)

# get_header('CS 70 Discrete Mathematics and Probability Theory Fall 2019 Alistair Sinclair and Yun Song Note 5 1 Graph Theory: An Introduction One of the fundamental ideas in computer science is the notion of abstraction: capturing the essence or the core of some complex situation by a simple model. Some of the largest and most complex entities we might deal wi')
