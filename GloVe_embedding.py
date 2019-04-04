from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from gensim.scripts.glove2word2vec import glove2word2vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from iteration_utilities import flatten
import gensim
from sklearn import svm, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

glove_input_file = '/Users/pengyuzhou/Downloads/glove.6B/glove.6B.100d.txt'
word2vec_output_file = '/Users/pengyuzhou/Downloads/glove.6B/glove.6B.100d.txt.word2vec'
# glove2word2vec(glove_input_file, word2vec_output_file)
encoding = "utf-8"

from gensim.models import KeyedVectors
import csv, alg_bayes, alg_decision_tree, alg_logestic_regression, alg_ramdom_forest, alg_svm
# numpy
import numpy, linkedindata, datafilter, globalparameter, random, labeled_data_sentence, linkedindata_old

linkedIndata_list = []
with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/data.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        parameter_list = [row[index] for index in range(67)]
        linkedIndata_list.append(
            linkedindata_old.LinkedInData(*parameter_list))

filename = '/Users/pengyuzhou/Downloads/word_embedding_result/total_data_model.d2v'
# model.save(filename)
for top_n_index in range(20,220,20):
    globalparameter.alg_precision = [0] * 48
    globalparameter.alg_recall = [0] * 48
    globalparameter.alg_accuracy = [0] * 48
    globalparameter.alg_f1_score = [0] * 48
    for i in range(6):
        print('Began to read job title: ' + globalparameter.jobtitle_list[i])
        relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list, globalparameter.jobtitle_list[i],
                                                                      1)
        non_relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list,
                                                                          globalparameter.jobtitle_list[i], 2)
        for j in range(5):
            print('began the iteration: ' + str(j + 1) + ' for job title: ' + globalparameter.jobtitle_list[i])
            pos_list = random.sample(relevant_user_list, 500)
            neg_list = random.sample(non_relevant_user_list, 500)

            # You can change the features you want to use
            pos_profile_list = []
            neg_profile_list = []
            for k in range(len(pos_list)):
                userprofile = ' '.join(pos_list[k].return_value_work_exp())
                pos_profile_list.append(userprofile)

            for k in range(len(neg_list)):
                userprofile = ' '.join(neg_list[k].return_value_work_exp())
                neg_profile_list.append(userprofile)

            pos_label_list = ['pos_profile_' + str(k) for k in range(len(pos_profile_list))]
            neg_label_list = ['neg_profile_' + str(k) for k in range(len(pos_profile_list))]
            pos_profile_list = [word for word in pos_profile_list if word not in stopwords.words('english')]
            neg_profile_list = [word for word in neg_profile_list if word not in stopwords.words('english')]
            X_pos, y_pos = [], []
            X_neg, y_neg = [], []
            for indexnum in range(len(pos_profile_list)):
                # texts are already tokenized, just split on space
                # in a real case we would use e.g. spaCy for tokenization
                # and maybe remove stopwords etc.
                X_pos.append([word for word in pos_profile_list[indexnum].split() if word not in stopwords.words('english')])
                y_pos.append(1)
            X_pos, y_pos = np.array(X_pos), np.array(y_pos)
            print("total pos examples %s" % len(y_pos))
            for indexnum in range(len(pos_profile_list)):
                # texts are already tokenized, just split on space
                # in a real case we would use e.g. spaCy for tokenization
                # and maybe remove stopwords etc.
                X_neg.append([word for word in neg_profile_list[indexnum].split() if word not in stopwords.words('english')])
                y_neg.append(0)
            # X_neg, y_neg = np.array(X_neg), np.array(y_neg)
            print("total neg examples %s" % len(y_neg))
            X_train = [X_pos[i] for i in range(250)] + [X_neg[i] for i in range(250)]
            Y_train = [y_pos[i] for i in range(250)] + [y_neg[i] for i in range(250)]
            X_test = [X_pos[i] for i in range(250,500)] + [X_neg[i] for i in range(250,500)]
            Y_test = [y_pos[i] for i in range(250,500)] + [y_neg[i] for i in range(250,500)]
            # for i in range(250):
            #     X_test = X_test+(X_pos[250+i])
            # for i in range(250):
            #     X_test = X_test+(X_neg[250+i])
            # for i in range(250):
            #     Y_test = Y_test+(y_pos[250+i])
            # for i in range(250):
            #     Y_test = Y_test+(y_neg[250+i])

            X_train = np.array(X_train)
            X_test = np.array(X_test)

            X_total = X_pos+X_neg
            glove_100d = {}
            all_words = set(w for words in X_total for w in words)
            with open(glove_input_file, "rb") as infile:
                for line in infile:
                    parts = line.split()
                    word = parts[0].decode(encoding)
                    if (word in all_words):
                        nums = np.array(parts[1:], dtype=np.float32)
                        glove_100d[word] = nums
            X_train_vectorized = []
            X_test_vectorized = []

            for indexnum in range(len(X_train)):
                if X_train[indexnum]:
                    new_X_train_profile = [
                        np.mean([glove_100d[words] for words in X_train[indexnum] if words in glove_100d] or [np.zeros(100)],axis=0).tolist()]
                    # print('length of X_train is'+str(new_X_train_profile.size))
                    new_X_train_profile = [val for val in new_X_train_profile[0]]

                    X_train_vectorized.append(new_X_train_profile)
                else:
                    X_train_vectorized.append(np.zeros(100).tolist())
            test1 = len(X_test)

            for indexnum1 in range(len(X_test)):
                if X_test[indexnum1]:
                    # new_X_test_profile = np.mean(np.array([
                    #     np.mean([glove_100d[w] for w in words if w in glove_100d] or [np.zeros(100)], axis=0) for words in X_test[indexnum]]),axis=0)
                    # X_test_vectorized.append(new_X_test_profile)
                    new_X_test_profile = [
                        np.mean([glove_100d[words] for words in X_test[indexnum1] if words in glove_100d] or [np.zeros(100)],axis=0).tolist()]
                    # print('length of X_test'+str(new_X_test_profile.size))
                    new_X_test_profile = [val for val in new_X_test_profile[0]]
                    X_test_vectorized.append(new_X_test_profile)

                else:
                    X_test_vectorized.append(np.zeros(100).tolist())

            # X_train_vectorized = np.array(X_train_vectorized)
            # Y_train = np.array(Y_train)
            # X_test_vectorized = np.array(X_test_vectorized)
            # Y_test = np.array(Y_test)
            # flatten the list
            flattened_X_train_vectorized = []
            flattened_X_test_vectorized = []
            # for i in range(len(X_train_vectorized)):
            #     flattened_X_train_vectorized.append([val for sublist in X_train_vectorized[i] for val in sublist])
            # for i in range(len(X_test_vectorized)):
            #     flattened_X_test_vectorized.append([val for sublist in X_test_vectorized[i] for val in sublist])


            alg_logestic_regression.calculate_logistic_regression(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_logestic_regression.calculate_logistic_regression_cv(X_train_vectorized, Y_train, X_test_vectorized, Y_test,
                                                                     i * 8,top_n_index)
            alg_svm.calculate_svm_linear_svc(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_svm.calculate_svm_nusvc(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_svm.calculate_svm_svc(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_bayes.calculate_bayes(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_decision_tree.calculate_decision_tree(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)
            alg_ramdom_forest.calculate_random_forest(X_train_vectorized, Y_train, X_test_vectorized, Y_test, i * 8,top_n_index)

            print('end this iteration')
        print('Switch to next job title.')

    for i in range(48):
        globalparameter.alg_precision[i] = (globalparameter.alg_precision[i]) / 5
        globalparameter.alg_recall[i] = (globalparameter.alg_recall[i]) / 5
        globalparameter.alg_accuracy[i] = (globalparameter.alg_accuracy[i]) / 5
        globalparameter.alg_f1_score[i] = (globalparameter.alg_f1_score[i]) / 5

    print('Precision value list: {}'.format(globalparameter.alg_precision))
    print('Recall value list: {}'.format(globalparameter.alg_recall))
    print('Accuracy value list: {}'.format(globalparameter.alg_accuracy))
    result_list = pd.DataFrame({'precision': globalparameter.alg_precision, 'recall': globalparameter.alg_recall,
                                'accuracy': globalparameter.alg_accuracy, 'f1_score': globalparameter.alg_f1_score})
    result_list.to_csv('/Users/pengyuzhou/Downloads/word2vec_average_sentence_result/all_result_list_top_'+str(top_n_index)+'.csv')
        # load the Stanford GloVe model
        # filename = '/Users/pengyuzhou/Downloads/glove.6B/glove.6B.100d.txt.word2vec'
        # model = KeyedVectors.load_word2vec_format(filename, binary=False)
        # calculate: (king - man) + woman = ?
    print(1)
