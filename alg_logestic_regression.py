import pandas as pd
import globalparameter, n_grams, csv, itertools, time
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import generate_train_test_set
from sklearn.metrics import recall_score
from numpy import genfromtxt
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_score, accuracy_score
from sklearn.decomposition import TruncatedSVD
import bag_of_words
import matplotlib.pyplot as plt


def logestic_regression(folderpath, jobtitle_path_list, ratio, sum_index):
    user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))

    X = user_profile[['normalized_work_year_past1', 'normalized_work_year_past2',
                      'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
                      'normalized_work_year_past6']]  # use highest degree, six past work experience
    Y = user_profile['normalized_now_relevant_job']
    # X_train = pd.concat(
    #     [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
    #         globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    # X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
    #     globalparameter.extract_number + (
    #             globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    Y_train = pd.concat(
        [Y.iloc[0:int(globalparameter.extract_number * ratio)], Y.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    Y_test = pd.concat([Y.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], Y.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])

    # generate matrix of bag-of-words
    matrix = bag_of_words.extractall_information(folderpath + '/' + 'output_pos_for_dummy.csv',
                                                 folderpath + '/' + 'output_neg_for_dummy.csv',
                                                 globalparameter.extract_skills_list)

    # generate matrix of 2-gram
    # matrix = n_grams.extractall_information_n_gram(folderpath + '/' + 'output_pos_for_dummy.csv',
    #                                                folderpath + '/' + 'output_neg_for_dummy.csv',
    #                                                globalparameter.extract_column_list, 2)

    # generate matrix of 3-gram
    # matrix = n_grams.extractall_information_n_gram(folderpath + '/' + 'output_pos_for_dummy.csv',
    #                                                folderpath + '/' + 'output_neg_for_dummy.csv',
    #                                                globalparameter.extract_skills_list, 3)

    X_train = generate_train_test_set.generate_X_train(matrix, X, ratio, globalparameter.train_pos_start_loc,
                                                       globalparameter.train_pos_end_loc,
                                                       globalparameter.train_neg_start_loc,
                                                       globalparameter.train_neg_end_loc)
    X_test = generate_train_test_set.generate_X_test(matrix, X, ratio, globalparameter.test_pos_start_loc,
                                                     globalparameter.test_pos_end_loc,
                                                     globalparameter.test_neg_start_loc,
                                                     globalparameter.test_neg_end_loc)

    len_xtrain = len(X_train)
    len_xtest = len(X_test)
    len_ytrain = len(Y_train)
    len_ytest = len(Y_test)
    sc = StandardScaler()
    isnull = np.isnan(X_train).any()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # train logestic regression
    logreg = linear_model.LogisticRegression()
    start_time = time.time()
    logreg.fit(X_train, Y_train)
    end_time = time.time()
    time_interval = end_time-start_time
    print('time_intervial is: {}'.format(time_interval))

    # predict
    Y_pred = logreg.predict((X_test))
    Y_pred_train = logreg.predict(X_train)
    Y_test_train = Y_train
    Y_test.index = range(int(globalparameter.total_number * (1 - ratio)))
    prepro = logreg.predict_proba(X_test_std)
    acc = logreg.score(X_test, Y_test)
    precision = precision_score(Y_test, Y_pred, labels=[0, 1], pos_label=1)
    recall = recall_score(Y_test, Y_pred,labels=[0, 1], pos_label=1)
    tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred).ravel()
    test_precision, test_recall, test_fscore, test_support = precision_recall_fscore_support(Y_test, Y_pred)
    train_precision, train_recall, train_fscore, train_support = precision_recall_fscore_support(Y_test_train,
                                                                                                 Y_pred_train)

    # print('prediction is : {}'.format(prediction))
    print('-------')
    print('Logestic regression')
    print('test_values are: {} {} {} {}'.format(test_precision, test_recall, test_fscore, test_support))
    print('train_values are: {} {} {} {}'.format(train_precision, train_recall, train_fscore, train_support))
    # print('confusing matrix is : tn:{} fp:{} fn:{} tp:{}'.format(tn, fp, fn, tp))
    # print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
    print('precision is: {}'.format(precision))
    print('recall is {}'.format(recall))

    globalparameter.alg_accuracy[sum_index+0] = globalparameter.alg_accuracy[sum_index+0] + acc
    globalparameter.alg_precision[sum_index+0] = globalparameter.alg_precision[sum_index+0] + precision
    globalparameter.alg_recall[sum_index+0] = globalparameter.alg_recall[sum_index+0] + recall
    globalparameter.time[sum_index+0] = globalparameter.time[sum_index+0] + time_interval


    Y_train = pd.concat(
        [Y.iloc[0:int(globalparameter.extract_number * ratio)], Y.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    Y_test = pd.concat([Y.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], Y.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    X_train = generate_train_test_set.generate_X_train(matrix, X, ratio, globalparameter.train_pos_start_loc,
                                                       globalparameter.train_pos_end_loc,
                                                       globalparameter.train_neg_start_loc,
                                                       globalparameter.train_neg_end_loc)
    X_test = generate_train_test_set.generate_X_test(matrix, X, ratio, globalparameter.test_pos_start_loc,
                                                     globalparameter.test_pos_end_loc,
                                                     globalparameter.test_neg_start_loc,
                                                     globalparameter.test_neg_end_loc)

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # train logestic regression
    logreg = linear_model.LogisticRegressionCV()
    start_time = time.time()
    logreg.fit(X_train, Y_train)
    end_time = time.time()
    time_interval = end_time-start_time
    print('time_intervial is: {}'.format(time_interval))

    # predict
    Y_pred = logreg.predict((X_test))
    Y_test.index = range(int(globalparameter.total_number * (1 - ratio)))
    prepro = logreg.predict_proba(X_test_std)
    acc = logreg.score(X_test, Y_test)
    acc_score = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred, labels=[0, 1], pos_label=1)
    recall = recall_score(Y_test, Y_pred,labels=[0, 1], pos_label=1)

    # print('prediction is : {}'.format(prediction))
    print('-------')
    print('Logestic regression CV')
    # print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
    print('precision is: {}'.format(precision))
    print('recall is {}'.format(recall))

    globalparameter.alg_accuracy[sum_index+1] = globalparameter.alg_accuracy[sum_index+1] + acc
    globalparameter.alg_precision[sum_index+1] = globalparameter.alg_precision[sum_index+1] + precision
    globalparameter.alg_recall[sum_index+1] = globalparameter.alg_recall[sum_index+1] + recall
    globalparameter.time[sum_index+1] = globalparameter.time[sum_index+1] + time_interval

    # # plot the diagram
    # precision, recall, _ = precision_recall_curve(Y_test, Y_score)
    #
    # # plt.step(recall, precision, color='pink', alpha=0.2, where='post')
    # plt.plot(recall, precision, label='logestic regression CV')
    # plt.xlabel('Recall')
    # plt.ylabel('Precision')
    # plt.ylim([0.0, 1.05])
    # plt.xlim([0.0, 1.0])
    # plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(avg_precesion))
    # plt.savefig(
    #     globalparameter.folderpath[1] + '/diagram_logestic_regression_p-r_' + globalparameter.jobtitle_path_list[
    #         1] + '-extract' + '.png')
