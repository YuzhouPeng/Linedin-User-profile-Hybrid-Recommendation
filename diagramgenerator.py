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
    id_manual_top500 = user_data['id'][:length].tolist()
    id_manual_other = user_data['id'][length:globalparameter.total_number].tolist()
    calculatewiththreshold(user_data, id_manual_top500, id_manual_other)

def calculatewiththreshold(user_data, id_manual_top500, id_manual_other):

    threshold = 0
    step = 0.001
    for i in range(1000):
        positive_test_cosine_similarity = user_data[user_data['cosine_similarity']>=threshold]['id'].tolist()
        negative_test_cosine_similarity = user_data[user_data['cosine_similarity']<threshold]['id'].tolist()

        positive_test_work_year = user_data[user_data['work_year']>=threshold]['id'].tolist()
        negative_test_work_year = user_data[user_data['work_year']<threshold]['id'].tolist()

        positive_test_highest_degree = user_data[user_data['highest_degree']>=threshold]['id'].tolist()
        negative_test_highest_degree = user_data[user_data['highest_degree']<threshold]['id'].tolist()

        positive_test_exp_time = user_data[user_data['exp_time']>=threshold]['id'].tolist()
        negative_test_exp_time = user_data[user_data['exp_time']<threshold]['id'].tolist()


        calculate(id_manual_top500, id_manual_other, positive_test_cosine_similarity,
                  negative_test_cosine_similarity, globalparameter.cosine_similarity_column_precision,
                  globalparameter.cosine_similarity_column_recall)
        calculate(id_manual_top500, id_manual_other, positive_test_work_year,
                  negative_test_work_year, globalparameter.work_year_column_precision,
                  globalparameter.work_year_column_recall)
        calculate(id_manual_top500, id_manual_other, positive_test_highest_degree,
                  negative_test_highest_degree, globalparameter.highest_degree_column_precision,
                  globalparameter.highest_degree_column_recall)
        calculate(id_manual_top500, id_manual_other, positive_test_exp_time,
                  negative_test_exp_time, globalparameter.exp_time_column_precision,
                  globalparameter.exp_time_column_recall)

        threshold = threshold + step


def calculate(positive, negative, positive_test, negative_test, precisionlist, recalllist):
    id_positive = positive
    id_negative = negative
    sorted_id_test_top500 = positive_test
    sorted_id_test_other = negative_test
    id_true_positive = []
    id_true_negative = []
    id_false_positive = []
    id_false_negative = []

    for i in range(len(sorted_id_test_other)):
        if sorted_id_test_other[i] in id_negative:
            id_true_negative.append(sorted_id_test_other[i])
    for i in range(len(sorted_id_test_top500)):
        if sorted_id_test_top500[i] in id_positive:
            id_true_positive.append(sorted_id_test_top500[i])
    for i in range(len(sorted_id_test_top500)):
        if sorted_id_test_top500[i] in id_negative:
            id_false_negative.append(sorted_id_test_top500[i])
    for i in range(len(sorted_id_test_other)):
        if sorted_id_test_other[i] in id_positive:
            id_false_positive.append(sorted_id_test_other[i])

    num_true_positive = len(id_true_positive)
    num_true_negative = len(id_true_negative)
    num_false_positive = len(id_false_positive)
    num_false_negative = len(id_false_negative)

    # print(len(id_false_positive))
    # print(len(id_false_negative))
    # print(id_false_positive)
    # print(id_false_negative)
    # print('accuracy = {}'.format((num_true_positive + num_true_negative) / 1000))
    # print('recall = {}'.format((num_true_positive) / (num_true_positive + num_false_negative)))
    # print('precision = {}'.format((num_true_positive) / (num_true_positive + num_false_positive)))
    # print()
    precisionlist.append((num_true_positive) / (num_true_positive + num_false_positive))
    recalllist.append((num_true_positive) / (num_true_positive + num_false_negative))


def generatediagram(precisionlist, recalllist, name_for_search, index,figureindex):
    plt.figure(figureindex)
    plt.title('Precision/Recall Curve: ' + name_for_search)  # give plot a title
    plt.xlabel('Recall')  # make axis labels
    plt.ylabel('Precision')

    x = precisionlist
    y = recalllist
    # f = open('eval.txt', 'r')
    # lines = f.readlines()
    # for i in range(len(lines) / 3):
    #     y.append(float(lines[3 * i].strip().split(':')[1]))
    #     x.append(float(lines[3 * i + 1].strip().split(':')[1]))
    # f.close()
    plt.figure(figureindex)
    plt.plot(x, y)
    plt.show()
    plt.savefig(globalparameter.path + '/p-r_' + name_for_search +'-extract'+ str(index) + '.png')
