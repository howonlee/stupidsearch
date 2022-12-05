import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import string
import sys
import operator

def normalized_pareto():
    res = npr.pareto(1, size=100)
    return res / res.sum()

def word_to_vec(word, alphabet):
    letters = list(word)
    res = np.zeros(100)
    for letter in letters:
        res += alphabet[letter]
    return res / res.sum()

def query(q, corpus_vecs, alph_vecs):
    q_vec = word_to_vec(q, alph_vecs)
    res = []
    for key, vec in corpus_vecs.items():
        sim = np.dot(q_vec, vec) / (npl.norm(q_vec) * npl.norm(vec))
        res.append([key, sim])
    return list(sorted(res, key=operator.itemgetter(1), reverse=True))

if __name__ == "__main__":
    corpus = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".lower().split()
    alphabet = list(string.ascii_lowercase)
    alph_vecs = {letter: normalized_pareto() for letter in alphabet}
    corpus_vecs = {word: word_to_vec(word, alph_vecs) for word in corpus}
    while True:
        q = input()
        print(query(q, corpus_vecs, alph_vecs)[:5])
        if q == "quit":
            sys.exit(0)
