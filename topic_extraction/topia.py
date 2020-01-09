# keyword extraction using topia - focuses on POS tagging and tokenization
# dependency: python –m pip install topia.termextract

# opening and extracting sample text files
with open('ochem.txt', 'r') as file:
    ochem = file.read().replace('\n', '')

with open('911.txt', 'r') as file:
    nine11 = file.read().replace('\n', '')

with open('rsa.txt', 'r') as file:
    rsa = file.read().replace('\n', '')

from topia.termextract import extract
from topia.termextract import tag

# Setup Term Extractor
extractor = extract.TermExtractor()

# Extract Keywords
keywords_topica = extractor(ochem)
print(keywords_topica)
