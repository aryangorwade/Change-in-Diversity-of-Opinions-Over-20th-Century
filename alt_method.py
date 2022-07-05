from flair.models import TextClassifier
from flair.data import Sentence
from nltk.corpus import PlaintextCorpusReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# compare opinions to clauses?

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
    if counter == 10:
        paras.append(current_para)
        current_para.clear()
        counter = 0

paragraph = Paragraph(x)

for i in range(6):
    print(paras[0])