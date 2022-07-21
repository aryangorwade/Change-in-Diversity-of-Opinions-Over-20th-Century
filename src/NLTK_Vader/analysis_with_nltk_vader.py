from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt
import re

# compare opinions to clauses?

# def getnumclauses(sentence):
    # first clean text (remove hyperlinks, @, etc)
    # then separate into clauses

def clean(sentence):
    result = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        " ", sentence)
    result1 = re.sub('@ ', '', result)
    return result1


def sentiment_analyze(category):
    corpus_root = r"C:\Users\user\PycharmProjects\NumOpinionsOver20thCentury\data_categorized" + category # Change address
    sentiment = SentimentIntensityAnalyzer()
    scores = []

    year = r"\19"
    counter = 0

    for x in range(10):
        temp = corpus_root + year + str(counter) + "0s"

        reader = PlaintextCorpusReader(temp, '.*')
        sents = reader.sents()
        sents1 = [[' '.join(i)] for i in sents]
        opinions = 0

        for x in sents1:
            cleaned = clean(x[0])
            sentiment_dict = sentiment.polarity_scores(cleaned)

            # change this block of code with each NLP library
            if sentiment_dict['compound'] >= 0.05 or sentiment_dict['compound'] <= - 0.05 :
                opinions = opinions + 1
                print("Opinion sent")
            else:
                print("Non opinion sent")

        numchars = len([char for sentence in reader.sents() for word in sentence for char in word])
        score = opinions / numchars
        scores.append(score)
        counter = counter + 1

    temp = corpus_root + r"\2000s"
    disp = 0

    reader = PlaintextCorpusReader(temp, '.*')
    sents = reader.sents()
    sents1 = [[' '.join(i)] for i in sents]
    opinions = 0

    for x in sents1:
        cleaned = clean(x[0])
        sentiment_dict = sentiment.polarity_scores(cleaned)

        # change this block of code with each NLP library
        if sentiment_dict['compound'] >= 0.05 or sentiment_dict['compound'] <= - 0.05:
            opinions = opinions + 1
            print("Opinion sent")
        else:
            print("Non opinion sent")

    numchars = len([char for sentence in reader.sents() for word in sentence for char in word])
    score = opinions / numchars
    scores.append(score)

    return scores

fiction_scores = sentiment_analyze(r"\Fiction")
magazine_scores = sentiment_analyze(r"\Magazine")
newspaper_scores = sentiment_analyze(r"\Newspaper")
years = ["1900s", "1910s", "1920s", "1930s", "1940s", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s"]

plt.plot(years, fiction_scores, label="Fiction")
plt.plot(years, magazine_scores, label="Magazine")
plt.plot(years, newspaper_scores, label="Newspaper")
plt.xlabel("Years")
plt.ylabel("Ratio of Opinions to Chars")
plt.title("Ratio of Opinions to Chars Over the 20th Century (NLTK-Vader)")
plt.legend()
plt.show()


