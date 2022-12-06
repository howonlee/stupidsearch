import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import string
import sys
import re
import itertools
import operator

def normalized_uniform():
    res = npr.uniform(size=100)
    return res / npl.norm(res)

def word_to_ngram_vec(word, ngrams, n):
    letters = list(word)
    word_ngrams = map(lambda x: "".join(x), zip(*[letters[i:] for i in range(n)]))
    res = np.zeros(100)
    for curr_ngram in word_ngrams:
        res += ngrams[curr_ngram]
    return res / npl.norm(res)

def query(q, corpus_vecs, ngram_vecs, n):
    q_vec = word_to_ngram_vec(q, ngram_vecs, n)
    res = []
    for key, vec in corpus_vecs.items():
        # normally we need to divide by npl norm but those are uniformly 1 because we made it so...
        # / (npl.norm(q_vec) * npl.norm(vec)) => put it back in if you'd like, no difference
        sim = np.dot(q_vec, vec)
        res.append([key, sim])
    return list(sorted(res, key=operator.itemgetter(1), reverse=True))

if __name__ == "__main__":
    n = 3
    with open("corpus.txt", "r") as corpus_file:
        unprocessed = corpus_file.read()
        no_unicode = re.sub(r'[^\x00-\x7f]', "", unprocessed)
        corpus = set(no_unicode.lower().split())
        alphabet = list(string.printable)
        ngram_vecs = {"".join(ngram): normalized_uniform() for ngram in itertools.product(alphabet, repeat=n)}
        corpus_vecs = {word: word_to_ngram_vec(word, ngram_vecs, n) for word in corpus}
        while True:
            q = input("Query: ")
            print("\n".join(map(str, query(q, corpus_vecs, ngram_vecs, n)[:5])))
            if q == "quit":
                sys.exit(0)
