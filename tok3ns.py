"""
SMALL MODULE FOR TOKENISING TEXT AND RETURNING A LIST
"""

import string

def tokenise(text, countTokens=False):
    noPunctuation = ''.join(c for c in text if c not in string.punctuation)
    noPunctuation.lower()
    tokens = noPunctuation.split()

    if countTokens:
        counter = len(tokens)
        return tokens, counter

    return tokens

