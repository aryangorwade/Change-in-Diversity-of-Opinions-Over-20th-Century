# from flair.models import TextClassifier
# from flair.data import Sentence
from textblob import TextBlob
from nltk.corpus import PlaintextCorpusReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

sample = "The sky is blue"
s
"""
flair_sentiment = TextClassifier.load('en-sentiment')
sentence = Sentence(sample)
flair_sentiment.predict(sentence)
score = sentence.labels[0]
print(score)
"""

print(getSubjectivity(sample))