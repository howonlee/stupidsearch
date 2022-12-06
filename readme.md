A Stupid Search
===

What's the most stupid natural text search possible that doesn't completely not work (viz., a search optimized for ease of implementation, not actual performance)? I reckon this one is pretty good.

Take your alphabet. Assign a random vector to each of them. For each document, for each letter, add up the corresponding vectors and normalize. That's the corresponding vector representation, no learning. Like a bag of words representations for letters, but way more suitable to direct cosine similarity query for some reason, probably because of the richness of the hyperspace that not being in the corners of the hypercube gives you.

But you can make the vector representation for queries. When you have a query, do the same. Take cosine distances, the top answers for cosine distances are the reults.

I didn't code-golf this but it's pretty obviously code-golfable.

There's another implementation with n-grams stuck in there too in ngrams.py.

Usage:

Put an ascii corpus in `corpus.txt` (nothing preventing it from working in unicode except a lot of necessary laziness...). The documents here are the individual words, it seems to work pretty materially worse for actual document-sized documents.

```python3 search.py```

Make queries.
