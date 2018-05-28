import pandas as pd
import globalparameter, csv, itertools
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score
import matplotlib.pyplot as plt


def logestic_regression(ratio):
    user_profile = pd.DataFrame(pd.read_csv(globalparameter.folderpath[1] + '/test1.csv'))

    X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
                      'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
                      'normalized_work_year_past6']]  # use highest degree, six past work experience
    Y = user_profile['normalized_now_relevant_job']
    X_train = pd.concat(
        [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    Y_train = pd.concat([Y.iloc[0:int(globalparameter.extract_number * ratio)], Y.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    Y_test = pd.concat([Y.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], Y.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])

    len_xtrain = len(X_train)
    len_xtest = len(X_test)
    len_ytrain = len(Y_train)
    len_ytest = len(Y_test)
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # train logestic regression
    logreg = linear_model.LogisticRegression()
    logreg.fit(X_train, Y_train)

    # predict
    prediction = logreg.predict((X_test))
    prepro = logreg.predict_proba(X_test_std)
    acc = logreg.score(X_test_std, Y_test)
    precision = precision_score(Y_test,prediction,labels=[0,1],pos_label=1)

    # print('prediction is : {}'.format(prediction))
    print('-------')
    print('Logestic regression')
    # print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
    print('precision is: {}'.format(precision))


    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    X_train = pd.concat(
        [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    Y_train = pd.concat([Y.iloc[0:int(globalparameter.extract_number * ratio)], Y.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    Y_test = pd.concat([Y.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], Y.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # train logestic regression
    logreg = linear_model.LogisticRegressionCV()
    logreg.fit(X_train, Y_train)

    # predict
    prediction = logreg.predict((X_test))
    prepro = logreg.predict_proba(X_test_std)
    acc = logreg.score(X_test_std, Y_test)
    precision = precision_score(Y_test,prediction,labels=[0,1],pos_label=1)

    # print('prediction is : {}'.format(prediction))
    print('-------')
    print('Logestic regression CV')
    # print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
    print('precision is: {}'.format(precision))

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
