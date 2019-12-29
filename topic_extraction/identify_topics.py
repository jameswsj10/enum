import nltk
import gensim
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# Topic identification python script for extracting a topic from one document

# We will use Latent Dirichlet Allocation for extracting the Topic
# First, we preprocess the raw text

# Tokenize and lemmatize
def preprocess(text):
    result=[]
    ps = PorterStemmer()
    for token in gensim.utils.simple_preprocess(text) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(ps.stem(token))
            # print(token, ": ", ps.stem(token))

    return result

# Converting text to bag of words
def filter_topics(text):
    processed_doc = preprocess(text)
    dictionary = gensim.corpora.Dictionary(processed_doc)
    bow_corpus = [dictionary.doc2bow(word) for word in processed_doc]
    for b in bow_corpus:
        print(b)

filter_topics(["""Markov chains are models of random motion in a finite or countable set. These models are powerful because
they capture a vast array of systems that we encounter in applications. Yet, the models are simple in that
many of their properties can often be determined using elementary matrix algebra. In this course, we limit
the discussion to the case of finite Markov chains, i.e., motions in a finite set."""])

# print(preprocess("""Markov chains are models of random motion in a finite or countable set. These models are powerful because
# they capture a vast array of systems that we encounter in applications. Yet, the models are simple in that
# many of their properties can often be determined using elementary matrix algebra. In this course, we limit
# the discussion to the case of finite Markov chains, i.e., motions in a finite set."""))
