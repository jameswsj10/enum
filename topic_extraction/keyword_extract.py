# opening and extracting sample text files
with open('ochem.txt', 'r') as file:
    ochem = file.read().replace('\n', '')

with open('911.txt', 'r') as file:
    nine11 = file.read().replace('\n', '')

with open('rsa.txt', 'r') as file:
    rsa = file.read().replace('\n', '')

#Source - https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0
# Author: Xu Liang - TextRank
from collections import OrderedDict
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load('en_core_web_sm')

class TextRank4Keyword():
    """Extract keywords from text"""

    def __init__(self):
        self.d = 0.85 # damping coefficient, usually is .85
        self.min_diff = 1e-5 # convergence threshold
        self.steps = 10 # iteration steps
        self.node_weight = None # save keywords and its weight


    def set_stopwords(self, stopwords):
        """Set stop words"""
        for word in STOP_WORDS.union(set(stopwords)):
            lexeme = nlp.vocab[word]
            lexeme.is_stop = True

    def sentence_segment(self, doc, candidate_pos, lower):
        """Store those words only in cadidate_pos"""
        sentences = []
        for sent in doc.sents:
            selected_words = []
            for token in sent:
                # Store words only with cadidate POS tag
                if token.pos_ in candidate_pos and token.is_stop is False:
                    if lower is True:
                        selected_words.append(token.text.lower())
                    else:
                        selected_words.append(token.text)
            sentences.append(selected_words)
        return sentences

    def get_vocab(self, sentences):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab

    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i+1, i+window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs

    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())

    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1

        # Get Symmeric matrix
        g = self.symmetrize(g)

        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm!=0) # this is ignore the 0 element in norm

        return g_norm


    def get_keywords(self, number=10):
        """Print top number keywords"""
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            print(key + ' - ' + str(value))
            if i > number:
                break


    def analyze(self, text,
                candidate_pos=['NOUN', 'PROPN', 'VERB'],
                window_size=4, lower=False, stopwords=list()):
        """Main function to analyze text"""
        # TODO: Filter text a bit more
        # filtering the text to contain only > 3 letter words OPTIONAL
        # text = ''.join(word for word in text if len(word) < 3)
        # print(text)

        # Set stop words
        self.set_stopwords(stopwords)

        # Pare text by spaCy
        doc = nlp(text)

        # Filter sentences
        sentences = self.sentence_segment(doc, candidate_pos, lower) # list of list of words

        # Build vocabulary
        vocab = self.get_vocab(sentences)

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1-self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr))  < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight
# text = """
# Four score and seven years ago our fathers brought forth, upon this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
#
# Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived, and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting-place for those who here gave their lives, that that nation might live. It is altogether fitting and proper that we should do this.
#
# But, in a larger sense, we can not dedicate, we can not consecrate we can not hallow this ground. The brave men, living and dead, who struggled here, have consecrated it far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here.
#
# It is for us, the living, rather, to be dedicated here to the unfinished work which they who fought here, have, thus far, so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion that we here highly resolve that these dead shall not have died in vain that this nation, under God, shall have a new birth of freedom and that government of the people, by the people, for the people, shall not perish from the earth.
# """
# text = """
# In data fitting, the task is to find a model, from a family of potential models,that best fits some observed data
# and prior information. Here the variables are the parameters in the model, and the constraints can represent prior
# information or required limits on the parameters (such as nonnegativity). The objective function might be a measure
# of misfit or prediction error between the observed data and the values predicted by the model, or a statistical measure
# of the unlikeliness orimplausibility of the parameter values. The optimization problem (1.1) is tofindthe model
# parameter values that are consistent with the prior information, and give the smallest misfit or prediction error
# with the observed dat
# """

text = """
WASHINGTON — President Trump backed away from further military action against Iran and called for renewed diplomacy on Wednesday as the bristling confrontation of the past six days eased in the aftermath of an Iranian missile strike that seemed intended to save face rather than inflict casualties.

“Iran appears to be standing down, which is a good thing for all parties concerned and a very good thing for the world,” Mr. Trump said in a televised statement from the Grand Foyer of the White House, flanked by his vice president, cabinet secretaries and senior military officers in their uniforms. “The United States,” he added, “is ready to embrace peace with all who seek it.”

The president sounded as eager as the Iranians to find a way out of a conflict that threatened to spiral out of control into a new full-fledged war in the Middle East. While Mr. Trump excoriated Iran’s “campaign of terror, murder, mayhem” and defended his decision to order a drone strike killing the country’s top security commander, he dropped for now his bombastic threats of escalating force, vowing instead to increase economic sanctions while calling for new negotiations.
"""
tr4w = TextRank4Keyword()
# analyze either rsa, nine11, or ochem string variables
tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN', 'ADJ', 'VERB'], window_size=4, lower=False)
tr4w.get_keywords(15)
