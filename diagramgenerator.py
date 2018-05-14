import pandas as pd
import globalparameter
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.feature_selection import RFECV

cosine_similarity_column_precision = []
cosine_similarity_column_recall = []
work_year_column_precision = []
work_year_column_recall = []
highest_degree_column_precision = []
highest_degree_column_recall = []
exp_time_column_precision = []
exp_time_column_recall = []


def calculateprecisionandrecall(extractnumber):
    length = extractnumber
    df = pd.read_csv(globalparameter.path + '/test1.csv', sep=',')
    id_column = df['normalized_id']
    index_column = df['index_normalized']
    cosine_similarity_column = df['normalized_cosine_similarity']
    work_year_column = df['normalized_work_year']
    highest_degree_column = df['normalized_highest_degree']
    exp_time_column = df['normalized_exp_time']
    user_data = pd.DataFrame(
        {'index': index_column, 'id': id_column, 'cosine_similarity': cosine_similarity_column,
         'work_year': work_year_column,
         'highest_degree': highest_degree_column, 'exp_time': exp_time_column})

    sorted_id_cosine_similarity = user_data.sort_values('cosine_similarity', ascending=False).groupby('id').head(500)
    sorted_id_cosine_similarity_top500 = sorted_id_cosine_similarity['id'][:length].tolist()
    sorted_id_cosine_similarity_other = sorted_id_cosine_similarity['id'][length:1000].tolist()

    sorted_id_work_year = user_data.sort_values('work_year', ascending=False).groupby('id').head(500)
    sorted_id_work_year_top500 = sorted_id_work_year['id'][:length].tolist()
    sorted_id_work_year_other = sorted_id_work_year['id'][length:1000].tolist()

    sorted_id_highest_degree = user_data.sort_values('highest_degree', ascending=False).groupby('id').head(500)
    sorted_id_highest_degree_top500 = sorted_id_highest_degree['id'][:length].tolist()
    sorted_id_highest_degree_other = sorted_id_highest_degree['id'][length:1000].tolist()

    sorted_id_exp_time = user_data.sort_values('exp_time', ascending=False).groupby('id').head(500)
    sorted_id_exp_time_top500 = sorted_id_exp_time['id'][:length].tolist()
    sorted_id_exp_time_degree_other = sorted_id_exp_time['id'][length:1000].tolist()

    cosine_similarity_top500 = user_data['id'].values[:length].tolist()
    cosine_similarity_other = user_data['id'].values[length:1000].tolist()

    work_year_top500 = sorted_id_work_year['id'][:length].tolist()
    id_manual_top500 = user_data['id'][:length].tolist()
    id_manual_other = user_data['id'][length:1000].tolist()

    calculate(id_manual_top500, id_manual_other, sorted_id_cosine_similarity_top500,
              sorted_id_cosine_similarity_other, extractnumber, globalparameter.cosine_similarity_column_precision,
              globalparameter.cosine_similarity_column_recall)
    calculate(id_manual_top500, id_manual_other, sorted_id_work_year_top500,
              sorted_id_work_year_other, extractnumber, globalparameter.work_year_column_precision,
              globalparameter.work_year_column_recall)
    calculate(id_manual_top500, id_manual_other, sorted_id_highest_degree_top500,
              sorted_id_highest_degree_other, extractnumber, globalparameter.highest_degree_column_precision,
              globalparameter.highest_degree_column_recall)
    calculate(id_manual_top500, id_manual_other, sorted_id_exp_time_top500,
              sorted_id_exp_time_degree_other, extractnumber, globalparameter.exp_time_column_precision,
              globalparameter.exp_time_column_recall)


def calculate(positive, negative, positive_test, negative_test, extract_number, precisionlist, recalllist):
    id_positive = positive
    id_negative = negative
    sorted_id_test_top500 = positive_test
    sorted_id_test_other = negative_test
    id_true_positive = []
    id_true_negative = []
    id_false_positive = []
    id_false_negative = []

    for i in range(1000-extract_number):
        if sorted_id_test_other[i] in id_negative:
            id_true_negative.append(sorted_id_test_other[i])
    for i in range(extract_number):
        if sorted_id_test_top500[i] in id_positive:
            id_true_positive.append(sorted_id_test_top500[i])
    for i in range(extract_number):
        if sorted_id_test_top500[i] in id_negative:
            id_false_negative.append(sorted_id_test_top500[i])
    for i in range(1000-extract_number):
        if sorted_id_test_other[i] in id_positive:
            id_false_positive.append(sorted_id_test_other[i])

    num_true_positive = len(id_true_positive)
    num_true_negative = len(id_true_negative)
    num_false_positive = len(id_false_positive)
    num_false_negative = len(id_false_negative)

    print(len(id_false_positive))
    print(len(id_false_negative))
    print(id_false_positive)
    print(id_false_negative)
    print('accuracy = {}'.format((num_true_positive + num_true_negative) / 1000))
    print('recall = {}'.format((num_true_positive) / (num_true_positive + num_false_negative)))
    print('precision = {}'.format((num_true_positive) / (num_true_positive + num_false_positive)))

    precisionlist.append((num_true_positive) / (num_true_positive + num_false_positive))
    recalllist.append((num_true_positive) / (num_true_positive + num_false_negative))


def generatediagram(precisionlist, recalllist, name_for_search):
    plt.figure(1)  # 创建图表1
    plt.title('Precision/Recall Curve')  # give plot a title
    plt.xlabel('Recall')  # make axis labels
    plt.ylabel('Precision')

    # x、y都是列表，里面存的分别是recall和precision
    # 传参得到或读取文件得到无所谓
    x = precisionlist
    y = recalllist
    # f = open('eval.txt', 'r')
    # lines = f.readlines()
    # for i in range(len(lines) / 3):
    #     y.append(float(lines[3 * i].strip().split(':')[1]))
    #     x.append(float(lines[3 * i + 1].strip().split(':')[1]))
    # f.close()
    plt.figure(1)
    plt.plot(x, y)
    plt.show()
    plt.savefig(globalparameter.path+'/p-r_'+name_for_search+'.png')

