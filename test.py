from flair.models import TextClassifier
from flair.data import Sentence
from nltk.corpus import PlaintextCorpusReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

corpus_root = r"C:\Users\user\PycharmProjects\NLP_Proj\data_categorized" + category
flair_sentiment = TextClassifier.load('en-sentiment')

    scores = []

paras = []
current_para = []
counter = 0

for x in sents1:
    current_para.append(x)
    counter = counter + 1
    if counter == 99:
        paras.append(current_para)
        current_para.clear()