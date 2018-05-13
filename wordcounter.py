# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:36:56 2018

@author: ypeng
"""
from __future__ import print_function
import globalparameter
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
import string
from scipy.sparse.csr import csr_matrix
import nltk

from nltk.corpus import stopwords
import nltk


def calculatetop100wordsofdoc():
    nltk.download("stopwords")
    stopWords = set(stopwords.words('english'))
    list1 = []
    with open(
            globalparameter.job_title_data_path) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row)
            words = new_row.split()
            for i in range(len(words)):
                if (words[i] not in stopWords):
                    list1.append(words[i])
                # string = new_row.translate(None, string.punctuation)

    counter = Counter(list1)
    print(d[0] for d in counter.most_common(100))
    top100list = list(counter.most_common(100))
    top100list_key = []
    for key, value in top100list:
        top100list_key.append(key)
    print(top100list_key)
    top100_string = ' '.join(top100list_key)
    print(top100_string)
    return top100_string

