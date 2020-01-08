import nltk
import gensim
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
#nltk.download('wordnet')      #download if using this module for the first timefrom nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#nltk.download('stopwords')    #download if using this module for the first time


#For Gensim
import gensim
import string
from gensim import corpora
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize

sample1 = """Introduction to Discrete Probability
Probability theory has its origins in gambling — analyzing card games, dice, roulette wheels. Today it is an
essential tool in engineering and the sciences. No less so in computer science, where its use is widespread
in algorithms, systems, learning theory and artificial intelligence.
Here are some typical statements that you might see concerning probability:
1. The chance of getting a flush in a 5-card poker hand is about 2 in 1000.
2. The chance that this randomized primality testing algorithm outputs “prime” when the input is not
prime is at most one in a trillion.
3. In this load-balancing scheme, the probability that any processor has to deal with more than 12 requests is negligible.
4. The average time between system failures is about 3 days.
5. There is a 30% chance of a magnitude 8.0 earthquake in Northern California before 2030.
Implicit in all such statements is the notion of an underlying probability space. This may be the result of a
random experiment that we have ourselves constructed (as in 1, 2 and 3 above), or some model we build of
the real world (as in 4 and 5 above). None of these statements makes sense unless we specify the probability
space we are talking about: for this reason, statements like 5 (which are typically made without this context)
are almost content-free.
In this note, we will try to understand all this more clearly. The first important notion here is that of a
random experiment. We will start by introducing the space of all possible outcomes of the experiment,
called a sample space. Each element of the sample space is assigned a probability which tells us how likely
the outcome is to occur when we actually perform the experiment."""
sample2 = """Conditional Probability, Independence, and Combinations of Events
One of the key properties of coin flips is independence: if you flip a fair coin ten times and get ten T’s, this
does not make it more likely that the next coin flip will be H’s. It still has exactly 50% chance of being H.
By contrast, suppose while dealing cards, the first ten cards are all red (hearts or diamonds). What is the
chance that the next card is red? We started with exactly 26 red cards and 26 black cards. But after dealing
the first ten cards, we know that the deck has 16 red cards and 26 black cards. So the chance that the
next card is red is 16
42 . So unlike the case of coin flips, now the chance of drawing a red card is no longer
independent of the previous card that was dealt. This is the phenomenon we will explore in this note on
conditional probability.
1 Conditional Probability"""
sample3 = """Random Variables: Distribution and Expectation
Recall our setup of a probabilistic experiment as a procedure of drawing a sample from a set of possible
values, and assigning a probability for each possible outcome of the experiment. For example, if we toss a
fair coin n times, then there are 2n possible outcomes, each of which is equally likely and has probability 1
2
n .
Now suppose we want to make a measurement in our experiment. For example, we can ask what is the
number of heads in n coin tosses; call this number X. Of course, X is not a fixed number, but it depends
on the actual sequence of coin flips that we obtain. For example, if n = 4 and we observe the outcome
ω = HT HH, then is X = 3; whereas if we observe the outcome ω = HT HT, then the is X = 2. In this
example of n coin tosses, we only know that X is an integer between 0 and n, but we do not know what its
exact value is until we observe which outcome of n coin flips is realized and count how many heads there
are. Because every possible outcome is assigned a probability, the value X also carries with it a probability
for each possible value it can take. The table below lists all the possible values X can take in the example of
n = 4 coin tosses, along with their respective probabilities."""
sample4 = """Random Variables: Variance and Covariance
We have seen in the previous note that if we take a biased coin that shows heads with probability p and toss
it n times, then the expected number of heads is np. What this means is that if we repeat the experiment
multiple times, where in each experiment we toss the coin n times, then on average we get np heads. But in
any single experiment, the number of heads observed can be any value between 0 and n. What can we say
about how far off we are from the expected value? That is, what is the typical deviation of the number of
heads from np?
1 Random Walk
Let us consider a simpler setting that is equivalent to tossing a fair coin n times, but is more amenable to
analysis. Suppose we have a particle that starts at position 0 and performs a random walk in one dimension.
At each time step, the particle moves either one step to the right or one step to the left with equal probability
(this kind of random walk is called symmetric), and the move at each time step is independent of all other
moves. We think of these random moves as taking place according to whether a fair coin comes up heads or
tails. The expected position of the particle after n moves is back at 0, but how far from 0 should we typically
expect the particle to end up?"""
sample5 = """Public Key Cryptography
In this note, we discuss a very nice and important application of modular arithmetic: the RSA public-key
cryptosystem, named after its inventors Ronald Rivest, Adi Shamir and Leonard Adleman.
The basic setting for cryptography is typically described via a cast of three characters: Alice and Bob, who
with to communicate confidentially over some (insecure) link, and Eve, an eavesdropper who is listening in
and trying to discover what they are saying. Let’s assume that Alice wants to transmit a message x (written
in binary) to Bob. She will apply her encryption function E to x and send the encrypted message E(x) over
the link; Bob, upon receipt of E(x), will then apply his decryption function D to it and thus recover the
original message: i.e., D(E(x)) = x.
Since the link is insecure, Alice and Bob have to assume that Eve may get hold of E(x). (Think of Eve
as being a “sniffer" on the network.) Thus ideally we would like to know that the encryption function E is
chosen so that just knowing E(x) (without knowing the decryption function D) doesn’t allow one to discover
anything about the original message x.
For centuries cryptography was based on what are now called private-key protocols. In such a scheme,
Alice and Bob meet beforehand and together choose a secret codebook, with which they encrypt all future
correspondence between them. (This codebook plays the role of the functions E and D above.) Eve’s only
hope then is to collect some encrypted messages and use them to at least partially figure out the codebook.
Public-key schemes such as RSA, first invented in the 1970s, are significantly more subtle and tricky: they
allow Alice to send Bob a message without ever having met him before! This almost sounds impossible,
because in this scenario there is a symmetry between Bob and Eve: why should Bob have any advantage over
Eve in terms of being able to understand Alice’s message? The central idea behind the RSA cryptosystem
is that Bob is able to implement a digital lock, to which only he has the key. Now by making this digital
lock public, he gives Alice (or, indeed, anybody else) a way to send him a secure message which only he
can open."""
# sample6 = "Interactive courses and projects."
# sample7 = "Personalized course recommendations from Iris."
# sample8 = "We’re excited to announce that Pluralsight has ranked #9 on the Great Place to Work 2018, Best Medium Workplaces list!"
# sample9 = "Few of the job opportunities include Implementation Consultant - Analytics, Manager - assessment production, Chief Information Officer, Director of Communications."

# compile documents
compileddoc = [sample1, sample2, sample3, sample4, sample5]

stopwords = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(document):
    stopwordremoval = " ".join([i for i in document.lower().split() if i not in stopwords])
    punctuationremoval = ''.join(ch for ch in stopwordremoval if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punctuationremoval.split())
    return normalized

final_doc = [clean(document).split() for document in compileddoc]

dictionary = corpora.Dictionary(final_doc)

DT_matrix = [dictionary.doc2bow(doc) for doc in final_doc]

Lda_object = gensim.models.ldamodel.LdaModel

lda_model_1 = Lda_object(DT_matrix, num_topics=5, id2word = dictionary)

print(lda_model_1.print_topics(num_topics=5, num_words=5))

# # nltk.download('punkt')
# # Topic identification python script for extracting a topic from one document
#
# # We will use Latent Dirichlet Allocation for extracting the Topic
# # First, we preprocess the raw text
#
# stopwords = set(stopwords.words('english'))
# exclude = set(string.punctuation)
# lemma = WordNetLemmatizer()
#
# # Clean function
# def clean(document):
#     stopwordremoval = " ".join([i for i in document.lower().split() if i not in stopwords])
#     punctuationremoval = ''.join(ch for ch in stopwordremoval if ch not in exclude)
#     normalized = " ".join(lemma.lemmatize(word) for word in punctuationremoval.split())
#     return normalized
#
# # Tokenize and lemmatize
# def preprocess(text):
#     result=[]
#     ps = PorterStemmer()
#     for token in gensim.utils.simple_preprocess(text) :
#         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
#             result.append(ps.stem(token))
#             # print(token, ": ", ps.stem(token))
#
#     return result
#
# # Converting text to bag of words
# def filter_topics(text):
#     processed_doc = preprocess(text)
#     dictionary = gensim.corpora.Dictionary(processed_doc)
#     bow_corpus = [dictionary.doc2bow(word) for word in processed_doc]
#     for b in bow_corpus:
#         print(b)
#
# filter_topics(["""Markov chains are models of random motion in a finite or countable set. These models are powerful because
# they capture a vast array of systems that we encounter in applications. Yet, the models are simple in that
# many of their properties can often be determined using elementary matrix algebra. In this course, we limit
# the discussion to the case of finite Markov chains, i.e., motions in a finite set."""])
#
# # print(preprocess("""Markov chains are models of random motion in a finite or countable set. These models are powerful because
# # they capture a vast array of systems that we encounter in applications. Yet, the models are simple in that
# # many of their properties can often be determined using elementary matrix algebra. In this course, we limit
# # the discussion to the case of finite Markov chains, i.e., motions in a finite set."""))
