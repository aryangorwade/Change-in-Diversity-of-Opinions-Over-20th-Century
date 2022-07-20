from textblob import TextBlob
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt
from sent_splitter_ordered import *;
import re
import time

# recheck program; results vary from before
# print a small segment of a few database lines to see if opinion judging is accurate
# how do words like "and" at the end of a clause affect whether it's an opinion?

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def clean(sentence):
    result = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        " ", sentence)
    result1 = re.sub('@ ', '', result)
    return result1

def sentiment_analyze(category):
    corpus_root = r"C:\Users\user\PycharmProjects\NLP_Proj\data_categorized" + category
    scores = []

    year = r"\19"
    counter = 0
    at = 0

    for x in range(10):
        temp = corpus_root + year + str(counter) + "0s"

        reader = PlaintextCorpusReader(temp, '.*')
        sents = reader.sents()
        sents1 = [[' '.join(i)] for i in sents]
        opinions = 0
        num_clauses = 0

        for x in sents1:
            cleaned = clean(x[0])
            clauses = sent_to_clauses(cleaned)
            num_clauses = num_clauses + len(clauses)

            for y in clauses:
                subjectivity = getSubjectivity(y)
                # change this block of code with each NLP library
                if subjectivity > 0.25:
                    opinions = opinions + 1
                else:
                    at = at + 1
                    print(at)
                    if (at == 100):
                        at = 0

        score = opinions / num_clauses
        scores.append(score)
        counter = counter + 1

    temp = corpus_root + r"\2000s"

    reader = PlaintextCorpusReader(temp, '.*')
    sents = reader.sents()
    sents1 = [[' '.join(i)] for i in sents]
    opinions = 0
    num_clauses = 0

    for x in sents1:
        cleaned = clean(x[0])
        clauses = sent_to_clauses(cleaned)
        num_clauses = num_clauses + len(clauses)

        for y in clauses:
            subjectivity = getSubjectivity(y)
            if subjectivity > 0.25:
                opinions = opinions + 1
            else:
                at = at + 1
                print(at)
                if (at == 100):
                    at = 0

    score = opinions / num_clauses
    scores.append(score)
    return scores

start_time  = time.time()
print("Started running at: " + str(start_time))

fiction_scores = sentiment_analyze(r"\Fiction")
magazine_scores = sentiment_analyze(r"\Magazine")
newspaper_scores = sentiment_analyze(r"\Newspaper")
years = ["1900s", "1910s", "1920s", "1930s", "1940s", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s"]

plt.plot(years, fiction_scores, label="Fiction")
plt.plot(years, magazine_scores, label="Magazine")
plt.plot(years, newspaper_scores, label="Newspaper")
plt.xlabel("Years")
plt.ylabel("Ratio of Opinions to Clauses")
plt.title("Ratio of Opinions to Clauses Over the 20th Century (TextBlob)")
plt.legend()
plt.show()

print("Stopped running at: " + time.time())
print("Program took", str(time.time() - start_time), "to run.")