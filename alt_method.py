from flair.models import TextClassifier
from flair.data import Sentence
from nltk.corpus import PlaintextCorpusReader
import re

from segtok.segmenter import split_single
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# compare opinions to clauses?

MAX_SENTENCES_IN_PARA = 5

def clean(raw):
    """ Remove hyperlinks and markup """
    result = re.sub("<[a][^>]*>(.+?)</[a]>", 'Link.', raw)
    result = re.sub('&gt;', "", result)
    result = re.sub('&#x27;', "'", result)
    result = re.sub('&quot;', '"', result)
    result = re.sub('&#x2F;', ' ', result)
    result = re.sub('<p>', ' ', result)
    result = re.sub('</i>', '', result)
    result = re.sub('&#62;', '', result)
    result = re.sub('<i>', ' ', result)
    result = re.sub("\n", '', result)
    return result

corpus_root = r"C:\Users\user\PycharmProjects\NLP_Proj\data_categorized\Fiction\1900s"
flair_sentiment = TextClassifier.load('en-sentiment')

scores = []
paras = []
current_para = []
counter = 0

reader = PlaintextCorpusReader(corpus_root, '.*')
sents = reader.sents()
sents1 = [[' '.join(i)] for i in sents]
opinions = 0
disp = 0

for x in sents1:
    current_para.append(x)
    counter = counter + 1
    if counter == MAX_SENTENCES_IN_PARA:
        paras.append(current_para)
        current_para = []
        counter = 0

for x in paras:
    para = []
    for i in range(len(x)):
        para = para + x[i]
    para_fixed = ' '.join(para)
    clean(para_fixed)
    sentence = Sentence(para_fixed)
    flair_sentiment.predict(sentence)

    score = sentence.labels[0]
    if "POSITIVE" in str(score) or "NEGATIVE" in str(score):
       opinions = opinions + 1
       print("Opinionated paragraph")

    else:
        print("Non-opinionated paragraph")

print(opinions)


