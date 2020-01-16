import nltk
import regex as re
# nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

# Suffix Stripping and known for simplicity and speed, may not be actual Eng word
def stemWord_porter(keyword):
    porter = PorterStemmer()
    return porter.stem(keyword)

# external linguistic rules, over-stemming may occur
def stemWord_lancaster(keyword):
    lancaster=LancasterStemmer()
    return lancaster.stem(keyword)


def single_word_match(text, stemmed_keyword):
    return (text.find(stemmed_keyword) > 0)


def fuzzymatch(text, keyword):
    # if len(keyword.split()) == 1:
    #     # stem the word, regex match it in the text
    #     # checks if stemmed_keyword is in text
    #     stemmed_keyword = lancaster.stem(keyword)
    #     return single_word_match(text, stemmed_keyword)
    # else:
    #     # stem the first word, regex match it in the text
    #     # go through all matches, then fuzzymatch the keyword phrase with the
    #     stemmed_keyword = stemWord_porter(keyword)
    #     if single_word_match(text, stemmed_keyword):
    #         for phrase in re.finditer("{}".format(stemmed_keyword), text):
    #             print(phrase)
    #     else:
    #         return False
    regex_pattern = []
    for word in keyword.split(" "):
        stemmed = stemWord_lancaster(word)
        regex_pattern.append(stemmed)
    # for matched_text in re.finditer()
    # return True if matches exist to keyword(s);


#def fuzzy_match(text, keyword):



#A list of words to be stemmed - compare contrast porter and lancaster
# source - https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
#word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
#print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
#for word in word_list:
#    print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))

# for checking if our fuzzymatch works
print(fuzzymatch("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""", "printing and typesetting"))
