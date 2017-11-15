# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:30:18 2017
"""
@author: DELL1

#intial model training code

import multiprocessing
#from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.word2vec import Word2Vec
#from gensim.models import TfidfModel
#from gensim.models.word2vec import LineSentence
import os


# logging is important to get the state of the functions
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

#wiki = WikiCorpus('data/enwiki-20170101-pages-articles-multistream.xml.bz2', lemmatize=False)
#tfidf = TfidfModel(wiki)
# save for persistence

#wiki.save('wiki.corpus')
#tfidf.save('wiki.tfidf.model')
          
# word2vec
sentences=[]

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
    file_path="enwiki-latest-pages-articles1.xml"
                
    with open(file_path,"r",buffering=1) as f:
                    for line in f:
                        sentences.append(line)

params = {'size': 200, 'window': 10, 'min_count': 10, 
          'workers': max(1, multiprocessing.cpu_count() - 1), 'sample': 1E-3,}
word2vec = Word2Vec(sentences, **params)
word2vec.save('wiki.word2vec.model')

print(word2vec.wv['configuration'])