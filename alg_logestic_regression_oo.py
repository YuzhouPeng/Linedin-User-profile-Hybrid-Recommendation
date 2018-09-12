import globalparameter
from sklearn import metrics
from sklearn import linear_model


def calculate_logistic_regression(X_train, Y_train, X_test, Y_test,sum_index,top_index):
    print('Algorithms: logistic regression')
    classifier = linear_model.LogisticRegression()
    classifier.fit(X_train, Y_train)
    prediction = classifier.predict(X_test)
    accuracy_score_p = metrics.accuracy_score(Y_test, prediction)
    accuracy_score = classifier.score(X_test, Y_test)
    precision_score = metrics.precision_score(Y_test, prediction)
    recall_score = metrics.recall_score(Y_test, prediction)
    f1_score = metrics.f1_score(Y_test,prediction)
    print('accuracy_score_p is : ' + str(accuracy_score_p))
    print('accuracy_score is : ' + str(accuracy_score_p))
    print('precision acore is :' + str(precision_score))
    print('recall score is :' + str(recall_score))
    print('f1_score is :'+str(f1_score))
    # calculate precision@n and recall@n
    precision_atn = 0
    recall_atn = 0
    if top_index!=0:
        recommend_relevant = 0
        for i in range(top_index):
            if prediction[i] == Y_test[i] and prediction[i] ==1:
                recommend_relevant = recommend_relevant+1
        precision_atn = recommend_relevant/top_index
        recall_atn = recommend_relevant/200
        print('precision@n acore is :' + str(precision_atn))
        print('recall@n score is :' + str(recall_atn))
    
    globalparameter.alg_accuracy[sum_index+0] = globalparameter.alg_accuracy[sum_index+0] + accuracy_score
    if top_index==0:
        globalparameter.alg_precision[sum_index+0] = globalparameter.alg_precision[sum_index+0] + precision_score
        globalparameter.alg_recall[sum_index+0] = globalparameter.alg_recall[sum_index+0] + recall_score
    globalparameter.alg_f1_score[sum_index+0] = globalparameter.alg_f1_score[sum_index+0] + f1_score
    if top_index!=0:
        globalparameter.alg_precision[sum_index+0] = globalparameter.alg_precision[sum_index+0] + precision_atn
        globalparameter.alg_recall[sum_index+0] = globalparameter.alg_recall[sum_index+0] + recall_atn
    
def calculate_logistic_regression_cv(X_train, Y_train, X_test, Y_test,sum_index,top_index):
    print('Algorithms: logistic regression CV')
    classifier = linear_model.LogisticRegressionCV()
    classifier.fit(X_train, Y_train)
    prediction = classifier.predict(X_test)
    accuracy_score_p = metrics.accuracy_score(Y_test, prediction)
    accuracy_score = classifier.score(X_test, Y_test)
    precision_score = metrics.precision_score(Y_test, prediction)
    recall_score = metrics.recall_score(Y_test, prediction)
    f1_score = metrics.f1_score(Y_test, prediction)
    print('accuracy_score_p is : ' + str(accuracy_score_p))
    print('accuracy_score is : ' + str(accuracy_score_p))
    print('precision acore is :' + str(precision_score))
    print('recall score is :' + str(recall_score))
    print('f1_score is :' + str(f1_score))

    # calculate precision@n and recall@n
    precision_atn = 0
    recall_atn = 0
    if top_index!=0:
        recommend_relevant = 0
        for i in range(top_index):
            if prediction[i] == Y_test[i] and prediction[i] ==1:
                recommend_relevant = recommend_relevant+1
        precision_atn = recommend_relevant/top_index
        recall_atn = recommend_relevant/200
        print('precision@n acore is :' + str(precision_atn))
        print('recall@n score is :' + str(recall_atn))

    globalparameter.alg_accuracy[sum_index + 1] = globalparameter.alg_accuracy[sum_index + 1] + accuracy_score
    if top_index==0:
        globalparameter.alg_precision[sum_index + 1] = globalparameter.alg_precision[sum_index + 1] + precision_score
        globalparameter.alg_recall[sum_index + 1] = globalparameter.alg_recall[sum_index + 1] + recall_score
    globalparameter.alg_f1_score[sum_index + 1] = globalparameter.alg_f1_score[sum_index + 1] + f1_score
    if top_index!=0:
        globalparameter.alg_precision[sum_index + 1] = globalparameter.alg_precision[sum_index + 1] + precision_atn
        globalparameter.alg_recall[sum_index + 1] = globalparameter.alg_recall[sum_index + 1] + recall_atn