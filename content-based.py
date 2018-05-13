#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:20:17 2018

@author: pengyuzhou
"""
from __future__ import print_function


import sklearn

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from collections import defaultdict
from sklearn.metrics.pairwise import linear_kernel
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
import warnings
import csv



v = TfidfVectorizer(min_df=1, stop_words='english')
episodes = defaultdict(list)
data = pd.read_csv('/Users/pengyuzhou/Google Drive/content-based-test/testdata-content-based.csv')
#print data['1']
data['1'] = data['1'].map(str.lower)
docs = data['1'].tolist()
tfidf1 = v.fit_transform(docs)
tfidf = tfidf1.toarray()

#feature_names = v.get_feature_names()
#print (feature_names)
cosine_similarities = linear_kernel(tfidf[0:1],tfidf).flatten()
cosine_similarities1 = linear_kernel(tfidf[0:1],tfidf[1:2]).flatten()

#print (cosine_similarities)
# give top n results
related_docs_indices = cosine_similarities.argsort()[:-500:-1]
i = 0
cosine_similarity_value = pd.DataFrame(cosine_similarities, columns = ['cosine_similarity_value']).to_csv('/Users/pengyuzhou/Desktop/software_engineer_cosine_similarity.csv')
related_doc_num = 0;
software_num = 501
for related_docs in related_docs_indices:
    i = i+1
    print("top data top :", i," is :", related_docs)
    if(related_docs)<software_num:
        related_doc_num = related_doc_num+1

result = cosine_similarities[related_docs_indices]
accuracy1 = (float)(related_doc_num-1)/500
print("accuracy: %.30f" %accuracy1)


## LSA
# lsa = TruncatedSVD(2, algorithm='arpack')
# tfidf1_lsa = lsa.fit_transform(tfidf1)
# tfidf1_lsa = Normalizer(copy=False).fit_transform(tfidf1_lsa)
# dataframe = pd.DataFrame(lsa.components_, index=["component_1", "component_2"], columns=v.get_feature_names())
# print(dataframe)
#
# dataframe1 = pd.DataFrame(tfidf1_lsa, index=docs, columns=["component_1", "component_2"])
# print(dataframe)


