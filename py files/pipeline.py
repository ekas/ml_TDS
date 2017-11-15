# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 05:55:46 2017

@author: DELL1
pipeline

"""
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import gensim
from gensim.models.word2vec import Word2Vec
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from matplotlib import pyplot

#Rule based

#Synonymys,hypernyms and probablistic
stop_words = set(stopwords.words('english'))
filtered_sentence=[]
corpus=[]


def word_extract(word_tokens):
    filtered_words=[]
    filtered_words = [w for w in word_tokens if w not in stop_words]    
    print(filtered_words)
    return filtered_words



sentences="charges for rendering houskeeping services , \n House keeping . !boys \n service charge"
tokenizer = RegexpTokenizer(r'\w+')
filtered_sentence.append(tokenizer.tokenize(sentences))
print(filtered_sentence)     

for j in range(len(filtered_sentence)):
    corpus.append(word_extract(filtered_sentence[j]))
    
model=gensim.models.Word2Vec.load("C:\\Users\\DELL1\\Desktop\\wiki.word2vec.model")
#model = Word2Vec.load_word2vec_format("C:\\Users\\DELL1\\Desktop\\wiki.word2vec.model", binary=True)
print("Word2Vec model loaded")

#b=['salary','boy','finance','counter','charges','women']
model.init_sims()
for i in range(len(corpus)):
    model = gensim.models.Word2Vec([corpus[i]],min_count=1,size=32)
    print(model.wv[corpus[i]]) 