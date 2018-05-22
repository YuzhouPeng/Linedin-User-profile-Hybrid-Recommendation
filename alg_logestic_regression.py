import pandas as pd
import numpy as np
import globalparameter, csv, itertools
from sklearn import preprocessing
import matplotlib.pyplot as plt
from numpy import genfromtxt

plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model, datasets
from sklearn.cross_validation import train_test_split


def logestic_regression():
    # # 1.加载数据
    # iris = datasets.load_iris()
    # X = iris.data[:, :2]  # 使用前两个特征
    # Y = iris.target
    # # np.unique(Y)   # out: array([0, 1, 2])
    #
    # # 2.拆分测试集、训练集。
    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    # # 设置随机数种子，以便比较结果。
    #
    # # 3.标准化特征值
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # sc.fit(X_train)
    # X_train_std = sc.transform(X_train)
    # X_test_std = sc.transform(X_test)
    #
    # # 4. 训练逻辑回归模型
    # logreg = linear_model.LogisticRegression(C=1e5)
    # logreg.fit(X_train, Y_train)
    #
    # # 5. 预测
    # prepro = logreg.predict_proba(X_test_std)
    # acc = logreg.score(X_test_std, Y_test)

    user_profile = pd.read_csv(globalparameter.folderpath[1]+'/test1.csv')
    # user_profile_highestdegree_array = []
    # user_profile_work_past1_array = []
    # user_profile_work_past2_array = []
    # user_profile_work_past3_array = []
    # user_profile_work_past4_array = []
    # user_profile_work_past5_array = []
    # user_profile_work_past6_array = []
    # user_rev_job = []
    # with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer/test.csv') as f:
    #     reader = csv.reader(f)
    #     for row in itertools.islice(reader, 1,1001):
    #         user_profile_highestdegree_array.append(row[2])
    #         user_profile_work_past1_array.append(row[5])
    #         user_profile_work_past2_array.append(row[6])
    #         user_profile_work_past3_array.append(row[7])
    #         user_profile_work_past4_array.append(row[8])
    #         user_profile_work_past5_array.append(row[9])
    #         user_profile_work_past6_array.append(row[10])
    #         user_rev_job.append(row[4])
    # user_profile_test = user_profile_highestdegree_array+user_profile_work_past1_array+user_profile_work_past2_array+user_profile_work_past3_array+user_profile_work_past4_array+user_profile_work_past5_array+user_profile_work_past6_array
    X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
                      'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
                      'normalized_work_year_past6']]  # use highest degree, six past work experience
    Y = user_profile['normalized_now_relevant_job']
    # np.unique(Y)   # out: array([0, 1, 2])

    # 2.拆分测试集、训练集。
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    # 设置随机数种子，以便比较结果。

    # 3.标准化特征值
    from sklearn.preprocessing import StandardScaler

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # 4. 训练逻辑回归模型
    logreg = linear_model.LogisticRegression(C=1e5)
    logreg.fit(X_train, Y_train)

    # 5. 预测
    prediction = logreg.predict((X_test_std))
    prepro = logreg.predict_proba(X_test_std)
    acc = logreg.score(X_test_std, Y_test)
    print('prediction is : {}'.format(prediction))
    print('-------')
    print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
