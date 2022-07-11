import spacy
import deplacy


def sent_to_clauses(text):
    en = spacy.load('en_core_web_sm')
    doc = en(text)
    deplacy.render(doc)

    seen = set() # keep track of covered words

    chunks = []
    for sent in doc.sents:
        heads = [cc for cc in sent.root.children if cc.dep_ == 'conj']

        for head in heads:
            words = [ww for ww in head.subtree]
            for word in words:
                seen.add(word)
            chunk = (' '.join([ww.text for ww in words]))
            chunks.append(chunk) # if clause list to be ordered properly, replace with --> chunks.append( (head.i, chunk) )

        unseen = [ww for ww in sent if ww not in seen]
        chunk = ' '.join([ww.text for ww in unseen])
        chunks.append(chunk)  # if clause list to be ordered properly, replace with --> chunks.append((sent.root.i, chunk))

#    chunks = sorted(chunks, key=lambda x: x[0]) <-- if clause list to be ordered properly, include

    return chunks

sent = "The ice cream is cold and is completely melted."
print(sent_to_clauses(sent))
