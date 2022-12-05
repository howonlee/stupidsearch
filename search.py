import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import string
import sys
import re
import operator

def normalized_uniform():
    res = npr.uniform(size=100)
    return res / npl.norm(res)

def word_to_vec(word, alphabet):
    letters = list(word)
    res = np.zeros(100)
    for letter in letters:
        res += alphabet[letter]
    return res / npl.norm(res)

def query(q, corpus_vecs, alph_vecs):
    q_vec = word_to_vec(q, alph_vecs)
    res = []
    for key, vec in corpus_vecs.items():
        # normally we need to divide by npl norm but those are uniformly 1 because we made it so...
        # / (npl.norm(q_vec) * npl.norm(vec)) => put it back in if you'd like, no difference
        sim = np.dot(q_vec, vec)
        res.append([key, sim])
    return list(sorted(res, key=operator.itemgetter(1), reverse=True))

if __name__ == "__main__":
    with open("corpus.txt", "r") as kjv_file:
        unprocessed = kjv_file.read()
        no_unicode = re.sub(r'[^\x00-\x7f]', "", unprocessed)
        corpus = set(no_unicode.lower().split())
        alphabet = list(string.printable)
        alph_vecs = {letter: normalized_uniform() for letter in alphabet}
        corpus_vecs = {word: word_to_vec(word, alph_vecs) for word in corpus}
        print(len(corpus))
        while True:
            q = input("Query: ")
            print("\n".join(map(str, query(q, corpus_vecs, alph_vecs)[:5])))
            if q == "quit":
                sys.exit(0)
