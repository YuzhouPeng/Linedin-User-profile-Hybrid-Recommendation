# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:36:56 2018

@author: ypeng
"""
from __future__ import print_function

import sklearn
from collections import Counter
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from collections import defaultdict
from sklearn.metrics.pairwise import linear_kernel
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
import numpy as np
import warnings
import csv
from scipy.sparse.csr import csr_matrix
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))
list1 = []
with open('C:/Users/ypeng/Dropbox/content-based-test/tf-idf-software_engineer_data_lower_case.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        new_row = ' '.join(row)
        words = new_row.split()
        for i in range(len(words)):
            if (words[i] not in stopWords):
                list1.append(words[i])
            # string = new_row.translate(None, string.punctuation)

counter = Counter(list1)

print(counter.most_common(100))