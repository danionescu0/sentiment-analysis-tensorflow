import numpy as np
import string


def normalize_text(dictionary: dict, text: str):
    document = []
    text = text.lower().encode('utf-8')
    words = text.split()
    for word in words:
        word = word.translate(None, string.punctuation.encode('utf-8'))
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0
        document.append(index)
    ln = 150 - len(document)
    if ln > 0 :
        document = np.pad(document, (0, ln), 'constant')
    return document
