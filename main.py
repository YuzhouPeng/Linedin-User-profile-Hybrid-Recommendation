import datanormalize, generateweightingfile, \
    datafilter, calculate_data_job_now, alg_logestic_regression, alg_svm, \
    alg_bayes, alg_decision_tree, alg_ramdom_forest, extract_multivalue_feature, generate_train_test_set, \
    calculate_baseline, bag_of_words, alg_logestic_regression_oo, alg_ramdom_forest_oo, alg_svm_oo, alg_bayes_oo, \
    alg_decision_tree_oo,n_grams
import globalparameter, csv, linkedindata, random
import time
import pandas as pd
from gensim.models import KeyedVectors


def datapreprocession():
    for i in range(6):
        datafilter.filter_alluser_with_newest_jobtitle(globalparameter.raw_data_path, globalparameter.folderpath[i],
                                                       globalparameter.jobtitle_path_list[i],
                                                       globalparameter.jobtitle_list[i])
    for i in range(6):
        calculate_data_job_now.calculate_work_year_except_newest(globalparameter.folderpath[i],
                                                                 globalparameter.folderpath[
                                                                     i] + '/' + globalparameter.jobtitle_path_list[
                                                                     i] + globalparameter.output_file_root,
                                                                 globalparameter.jobtitle_path_list[i],
                                                                 globalparameter.jobtitle_list[i])
        calculate_data_job_now.calculate_work_year_except_newest(globalparameter.folderpath[i],
                                                                 globalparameter.folderpath[
                                                                     i] + '/non_' + globalparameter.jobtitle_path_list[
                                                                     i] + globalparameter.output_file_root,
                                                                 '/non_' + globalparameter.jobtitle_path_list[i],
                                                                 globalparameter.jobtitle_list[i])


def normalizing_data():
    for i in range(6):
        print('generating weighting file of: ' + str(globalparameter.jobtitle_path_list[i]))
        generateweightingfile.generateweighting_expect_newest(globalparameter.extract_number,
                                                              globalparameter.folderpath[i],
                                                              globalparameter.jobtitle_path_list[i])
        print('normalizing weighting of ' + str(globalparameter.jobtitle_path_list[i]))
        datanormalize.normalize_weighting_highest_degree(globalparameter.folderpath[i] + '/test.csv',
                                                         globalparameter.folderpath[i])


def contentbased_old():
    # datapreprocession()
    for k in range(5):
        normalizing_data()
        j = 0
        for i in range(6):
            print('start iteration ' + str(i))
            print('------job title is:------')
            print(globalparameter.jobtitle_path_list[i])
            print('baseline precision value of job title is: ')
            calculate_baseline.baseline_full_text(globalparameter.jobtitle_list[i],
                                                  globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
                                                  globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
            calculate_baseline.baseline_work_exp(globalparameter.jobtitle_list[i],
                                                 globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
                                                 globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
            alg_logestic_regression.logestic_regression(globalparameter.folderpath[i],
                                                        globalparameter.jobtitle_path_list[i], 0.5, j)
            alg_svm.svm_classification(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5, j)
            alg_bayes.naive_bayes(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5, j)
            alg_decision_tree.decision_tree(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5,
                                            j)
            alg_ramdom_forest.random_forest(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5,
                                            j)
            j = j + 8
            print('------------')
        # words_list = bag_of_words.extractall_information(globalparameter.folderpath[0]+'/'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,globalparameter.folderpath[0]+'/non_'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,0,
        #     int(globalparameter.extract_number * 0.5), globalparameter.extract_number,
        #     globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * 0.5),globalparameter.extract_column_list)
        print(1)
    for i in range(48):
        globalparameter.alg_precision[i] = (globalparameter.alg_precision[i]) / 5
        globalparameter.alg_recall[i] = (globalparameter.alg_recall[i]) / 5
        globalparameter.alg_accuracy[i] = (globalparameter.alg_accuracy[i]) / 5
        globalparameter.time[i] = (globalparameter.time[i]) / 5

    print('Precision value list: {}'.format(globalparameter.alg_precision))
    print('Recall value list: {}'.format(globalparameter.alg_recall))
    print('Accuracy value list: {}'.format(globalparameter.alg_accuracy))
    result_list = pd.DataFrame({'precision': globalparameter.alg_precision, 'recall': globalparameter.alg_recall,
                                'accuracy': globalparameter.alg_accuracy, 'time': globalparameter.time})
    result_list.to_csv('/Users/pengyuzhou/Google Drive/Linkedin_datafile/all_result_list.csv')
    print()


def bag_of_words_oo(pos_list,neg_list):
    print('start bag-of-words feature representation')
    pos_list_data = bag_of_words.extract_information_oo(pos_list)
    neg_list_data = bag_of_words.extract_information_oo(neg_list)

    total_data = pos_list_data + neg_list_data

    bag_of_words_dummy = pd.get_dummies(pd.DataFrame(total_data), drop_first=True)
    X_train_set = pd.concat([bag_of_words_dummy.iloc[:250],
                           bag_of_words_dummy.iloc[500:750]])
    X_test_set = pd.concat([bag_of_words_dummy.iloc[250:500],
                          bag_of_words_dummy.iloc[750:1000]])

    X_train_set.index = range(500)
    X_test_set.index = range(500)

    Y_train = [1]*250 + [0]*250
    Y_test = [1]*250 + [0]*250
    top_n_index = 0
    # calculate the precision using different machine learning model
    alg_logestic_regression_oo.calculate_logistic_regression(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                             top_n_index)
    alg_logestic_regression_oo.calculate_logistic_regression_cv(X_train_set, Y_train, X_test_set, Y_test,
                                                                job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_linear_svc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_nusvc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_svc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_bayes_oo.calculate_bayes(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_decision_tree_oo.calculate_decision_tree(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                 top_n_index)
    alg_ramdom_forest_oo.calculate_random_forest(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                 top_n_index)

    print(1)

def n_grams_oo(pos_list,neg_list):
    print('start n-gram feature representation')
    pos_list_gram_data = n_grams.extract_information_n_grams_oo(pos_list,2)
    neg_list_gram_data = n_grams.extract_information_n_grams_oo(neg_list,2)


    total_data = pos_list_gram_data + neg_list_gram_data

    n_gram_dummy = pd.get_dummies(pd.DataFrame(total_data), drop_first=True)
    X_train_set = pd.concat([n_gram_dummy.iloc[:250],
                           n_gram_dummy.iloc[500:750]])
    X_test_set = pd.concat([n_gram_dummy.iloc[250:500],
                          n_gram_dummy.iloc[750:1000]])

    X_train_set.index = range(500)
    X_test_set.index = range(500)

    Y_train = [1]*250 + [0]*250
    Y_test = [1]*250 + [0]*250
    top_n_index = 0
    # calculate the precision using different machine learning model
    alg_logestic_regression_oo.calculate_logistic_regression(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                             top_n_index)
    alg_logestic_regression_oo.calculate_logistic_regression_cv(X_train_set, Y_train, X_test_set, Y_test,
                                                                job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_linear_svc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_nusvc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_svm_oo.calculate_svm_svc(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_bayes_oo.calculate_bayes(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8, top_n_index)
    alg_decision_tree_oo.calculate_decision_tree(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                 top_n_index)
    alg_ramdom_forest_oo.calculate_random_forest(X_train_set, Y_train, X_test_set, Y_test, job_iter_index * 8,
                                                 top_n_index)

    print(1)

if __name__ == '__main__':
    # main function

    # contentbased_old()

    # Object Oriented(OO) based method
    # initiate LinkedIn user data
    linkedIndata_list = []
    job_iter_index = 0
    with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/data_v3.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            parameter_list = [row[index] for index in range(112)]
            linkedIndata_list.append(
                linkedindata.LinkedInData(*parameter_list))
    # extract year by regular expression
    test_list = calculate_data_job_now.calculate_work_year_oo(linkedIndata_list)
    length_of_test_set = len(test_list[0])
    length_of_linkedindata = len(linkedIndata_list)
    for i in range(len(test_list[0])):
        linkedIndata_list[i].getworkdurationvalue(*[test_list[k][i] for k in range(10)])


    # iterate 6 selected job title in globalparameter.py

    for job_iter_index in range(6):
        print('Began to read job title: ' + globalparameter.jobtitle_list[job_iter_index])

        # data filter
        relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list, globalparameter.jobtitle_list[job_iter_index],
                                                                      1)
        non_relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list,
                                                                          globalparameter.jobtitle_list[job_iter_index], 2)
        length_relevant_user = len(relevant_user_list)
        length_non_relevant_user = len(non_relevant_user_list)

        # calculate values of evaluation metrics for 5 times

        for iterate in range(5):
            # iterations for calculate average precision
            pos_list = random.sample(relevant_user_list, 500)
            neg_list = random.sample(non_relevant_user_list, 500)

            # test feature representation of bag-of-words

            bag_of_words_oo(pos_list,neg_list)

            # test feature representation of n-grams

            # n_grams_oo(pos_list,neg_list)

            print('end this iteration')
        print('switch to next job title')

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
    result_list.to_csv('/Users/pengyuzhou/Downloads/word2vec_average_sentence_result/rresult_list_oo'+'.csv')
        # load the Stanford GloVe model
        # filename = '/Users/pengyuzhou/Downloads/glove.6B/glove.6B.100d.txt.word2vec'
        # model = KeyedVectors.load_word2vec_format(filename, binary=False)
        # calculate: (king - man) + woman = ?
    print(1)
