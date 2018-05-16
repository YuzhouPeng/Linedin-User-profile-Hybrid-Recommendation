from __future__ import print_function
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from sklearn.metrics.pairwise import linear_kernel
import csv, string, globalparameter, wordcounter
import itertools
import pandas as pd


def content_based_doc_generator(extract_number):
    new_csv_file = []
    top100string = wordcounter.calculatetop100wordsofdoc()
    # writer = csv.writer(globalparameter.path + '/cosinesimilarity_test.csv')
    with open(globalparameter.path + '/cosinesimilarity_test.csv', 'w') as g:
        with open(globalparameter.job_title_data_path) as f:
            reader = csv.reader(f)
            writer = csv.writer(g)
            writer.writerow([1])
            writer.writerow([top100string])
            for row in itertools.islice(reader, extract_number):
                new_row = ' '.join(row[3:66])
                writer.writerow([new_row])
        with open(globalparameter.non_job_title_data_path) as f1:
            reader1 = csv.reader(f1)
            for row in itertools.islice(reader1, globalparameter.total_number-extract_number):
                new_row = ' '.join(row[3:66])
                writer.writerow([new_row])

def calculatecosinesililarity():
    v = TfidfVectorizer(min_df=1, stop_words='english')
    episodes = defaultdict(list)
    data = pd.read_csv(globalparameter.path+'/cosinesimilarity_test.csv')
    # print data['1']
    data['1'] = data['1'].map(str.lower)
    docs = data['1'].tolist()
    tfidf1 = v.fit_transform(docs)
    tfidf = tfidf1.toarray()

    # feature_names = v.get_feature_names()
    # print (feature_names)
    cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
    cosine_similarities1 = linear_kernel(tfidf[0:1], tfidf[1:2]).flatten()

    # print (cosine_similarities)
    # give top n results
    # related_docs_indices = cosine_similarities.argsort()[:-500:-1]
    i = 0
    cosine_similarity_value = pd.DataFrame(cosine_similarities, columns=['cosine_similarity_value']).to_csv(
        globalparameter.path+globalparameter.output_file_header_job_title+'cosine_similarity_test.csv')
    # related_doc_num = 0;
    # software_num = 501
    # for related_docs in related_docs_indices:
    #     i = i + 1
    #     # print("top data top :", i, " is :", related_docs)
    #     if (related_docs) < software_num:
    #         related_doc_num = related_doc_num + 1
    #
    # result = cosine_similarities[related_docs_indices]
    # accuracy1 = (float)(related_doc_num - 1) / 500
    # print("accuracy: %.30f" % accuracy1)