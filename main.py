from flair.models import TextClassifier
from flair.data import Sentence
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt

# TODO: recheck program; results vary from before
# compare opinions to clauses?

def sentiment_analyze(category):
    corpus_root = r"C:\Users\user\PycharmProjects\NLP_Proj\data_categorized" + category
    flair_sentiment = TextClassifier.load('en-sentiment')

    scores = []

    year = r"\19"
    counter = 0

    for x in range(10):
        temp = corpus_root + year + str(counter) + "0s"

        reader = PlaintextCorpusReader(temp, '.*')
        sents = reader.sents()
        sents1 = [[' '.join(i)] for i in sents]
        opinions = 0
        disp = 0

        for x in sents1:
            sentence = Sentence(x)
            flair_sentiment.predict(sentence)
            score = sentence.labels[0]
            # TODO: change this block of code with flair
            if "POSITIVE" in str(score) or "NEGATIVE" in str(score):
                opinions = opinions + 1
                disp = disp + 1
                if disp >= 100:
                    disp = 0
                print(disp)

        numchars = len([char for sentence in reader.sents() for word in sentence for char in word])
        score = opinions / numchars
        scores.append(score)
        counter = counter + 1

    temp = corpus_root + r"\2000s"
    counter = 1
    disp = 0

    reader = PlaintextCorpusReader(temp, '.*')
    sents = reader.sents()
    sents1 = [[' '.join(i)] for i in sents]
    opinions = 0

    for x in sents1:
        sentence = Sentence(x)
        flair_sentiment.predict(sentence)
        score = sentence.labels[0]
        # TODO: change this block of code with flair
        if "POSITIVE" in str(score) or "NEGATIVE" in str(score):
            opinions = opinions + 1
            disp = disp + 1
            if disp >= 100:
                disp = 0
            print(disp)

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
plt.title("Ratio of Opinions to Chars Over the 20th Century")
plt.legend()
plt.show()


