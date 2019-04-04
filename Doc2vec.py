from gensim.models import KeyedVectors
import csv,alg_bayes,alg_decision_tree,alg_logestic_regression,alg_ramdom_forest,alg_svm
import pandas as pd
# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
# numpy
import numpy,linkedindata,datafilter,globalparameter, random,labeled_data_sentence,linkedindata_old
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
# random
from random import shuffle
# classifier
from sklearn.linear_model import LogisticRegression
#
# filename = '/Users/pengyuzhou/Downloads/GoogleNews-vectors-negative300.bin'
# model = KeyedVectors.load_word2vec_format(filename, binary=True)
# csvfile = csv.reader(open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/data.csv',"r"))

linkedIndata_list = []
with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/data.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        parameter_list = [row[index] for index in range(67)]
        linkedIndata_list.append(
            linkedindata_old.LinkedInData(*parameter_list))
# train the model
# total_user_profile = []
# for i in range(len(linkedIndata_list)):
#     user_profile = ' '.join(linkedIndata_list[i].return_value_all())
#     total_user_profile.append(user_profile)
# documents = labeled_data_sentence.LabeledLineSentence(total_user_profile, ['sentence_'+ str(i) for i in range(len(linkedIndata_list))])
# model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
# model.build_vocab(documents.to_array())
# for epoch in range(20):
#     model.train(documents.sentences_perm(), total_examples=model.corpus_count, epochs=model.iter)
filename = '/Users/pengyuzhou/Downloads/word_embedding_result/total_data_model.d2v'
# model.save(filename)

for i in range(6):
    print('Began to read job title: '+ globalparameter.jobtitle_list[i])
    relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list, globalparameter.jobtitle_list[i],
                                                                  1)
    non_relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list,
                                                                      globalparameter.jobtitle_list[i], 2)
    for j in range(5):
        print('began the iteration: '+str(j+1)+' for job title: '+globalparameter.jobtitle_list[i])
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

        pos_label_list = ['pos_profile_'+ str(k) for k in range(len(pos_profile_list))]
        neg_label_list = ['neg_profile_'+ str(k) for k in range(len(pos_profile_list))]

        # documents = labeled_data_sentence.LabeledLineSentence(pos_profile_list,pos_label_list,neg_profile_list,neg_label_list)
        # model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
        # model.build_vocab(documents.to_array())
        # for epoch in range(20):
        #     model.train(documents.sentences_perm(), total_examples=model.corpus_count, epochs=model.iter)
        #     # model.train(documents.sentences_perm())
        # filename = '/Users/pengyuzhou/Downloads/word_embedding_result/job_title_'+globalparameter.jobtitle_list[i]+'.d2v'
        # model.save(filename)
        # filename = '/Users/pengyuzhou/Downloads/glove.6B/glove.6B.100d.txt.word2vec'
        model = Doc2Vec.load(filename)

        pos_vector_list = []
        neg_vector_list = []
        for x in range(len(pos_list)):
            pos_vector_list.append(model.infer_vector(pos_profile_list[x]))
        for x in range(len(neg_list)):
            neg_vector_list.append(model.infer_vector(neg_profile_list[x]))

        # model = Doc2Vec.load('/Users/pengyuzhou/Downloads/word_embedding_result/job_title_'+globalparameter.jobtitle_list[i]+'.d2v')

        test2 = model.most_similar('software')

        train_arrays = numpy.zeros((500,100))
        train_labels = numpy.zeros(500)

        for k in range(250):
            prefix_pos_train = 'pos_profile_'+ str(k)
            prefix_neg_train = 'neg_profile_'+ str(k)
            train_arrays[k] = pos_vector_list[k]
            train_arrays[250+k] = neg_vector_list[k]
            train_labels[k] = 1
            train_labels[250+k] = 0

        test_arrays = numpy.zeros((500, 100))
        test_labels = numpy.zeros(500)
        for k in range(250):
            prefix_test_pos = 'pos_profile_' + str(250+k)
            prefix_test_neg = 'neg_profile_' + str(250+k)
            test_arrays[k] = pos_vector_list[250+k]
            test_arrays[250 + k] = neg_vector_list[250+k]
            test_labels[k] = 1
            test_labels[250 + k] = 0

        alg_logestic_regression.calculate_logistic_regression(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_logestic_regression.calculate_logistic_regression_cv(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_svm.calculate_svm_linear_svc(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_svm.calculate_svm_nusvc(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_svm.calculate_svm_svc(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_bayes.calculate_bayes(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_decision_tree.calculate_decision_tree(train_arrays,train_labels,test_arrays,test_labels,i*8)
        alg_ramdom_forest.calculate_random_forest(train_arrays,train_labels,test_arrays,test_labels,i*8)

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
result_list.to_csv('/Users/pengyuzhou/Downloads/word_embedding_result/all_result_list.csv')

# classifier = LogisticRegression()
# classifier.fit(train_arrays, train_labels)
# prediction = classifier.predict(test_arrays)
# accuracy_score_p = accuracy_score(test_labels,prediction)
# accuracy_score = classifier.score(test_arrays, test_labels)
# precision_score = precision_score(test_labels,prediction)
# recall_score = recall_score(test_labels,prediction)
# 
# print('accuracy_score_p is : '+str(accuracy_score_p))
# print('accuracy_score is : '+ str(accuracy_score_p))
# print('precision acore is :' + str(precision_score))
# print('recall score is :' + str(recall_score))


print(1)