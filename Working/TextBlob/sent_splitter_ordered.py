"""
Credit for 'sent_to_clauses': polm23 (https://stackoverflow.com/users/355715/polm23)
Original code posted to stackoverflow: https://stackoverflow.com/questions/65227103/clause-extraction-long-sentence-segmentation-in-python
"""

import string
import spacy
# import deplacy

def sent_to_clauses(text):
    en = spacy.load('en_core_web_sm')
    doc = en(text)
#    deplacy.render(doc)

    seen = set() # keep track of covered words

    chunks = []
    for sent in doc.sents:
        heads = [cc for cc in sent.root.children if cc.dep_ == 'conj']

        for head in heads:
            words = [ww for ww in head.subtree]
            for word in words:
                seen.add(word)
            chunk = (' '.join([ww.text for ww in words]))
            chunks.append( (head.i, chunk) )

        unseen = [ww for ww in sent if ww not in seen]
        chunk = ' '.join([ww.text for ww in unseen])
        chunks.append((sent.root.i, chunk))

        chunks = sorted(chunks, key=lambda x: x[0])

        # edits I made that deviate from the original code are below
        final = []

        for x in chunks:
            temp = x[1]
            temp1 = temp.translate(str.maketrans('', '', string.punctuation))
            final.append(temp1)

    return final
