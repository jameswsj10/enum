import nltk
# nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter = PorterStemmer()
lancaster=LancasterStemmer()

# Suffix Stripping and known for simplicity and speed, may not be actual Eng word
def stemWord_porter(keyword):
    porter = PorterStemmer()
    return porter.stem(keyword)

# external linguistic rules, over-stemming may occur
def stemWord_lancaster(keyword):
    lancaster=LancasterStemmer()
    return lancaster.stem(keyword)

#A list of words to be stemmed - compare contrast porter and lancaster
# source - https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))
