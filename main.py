import datanormalize, generateweightingfile, \
    datafilter, calculate_data_job_now, alg_logestic_regression, alg_svm, \
    alg_bayes, alg_decision_tree, alg_ramdom_forest, extract_multivalue_feature, generate_train_test_set, \
    calculate_baseline, bag_of_words
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
            print('start iteration '+str(i))
            print('------job title is:------')
            print(globalparameter.jobtitle_path_list[i])
            print('baseline precision value of job title is: ')
            calculate_baseline.baseline_full_text(globalparameter.jobtitle_list[i],globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
                                                       globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
            calculate_baseline.baseline_work_exp(globalparameter.jobtitle_list[i],globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
                                                       globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
            # alg_logestic_regression.logestic_regression(globalparameter.folderpath[i],
            #                                             globalparameter.jobtitle_path_list[i], 0.5, j)
            # alg_svm.svm_classification(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5, j)
            # alg_bayes.naive_bayes(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5, j)
            # alg_decision_tree.decision_tree(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5,
            #                                 j)
            # alg_ramdom_forest.random_forest(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5,
            #                                 j)
            # j = j + 8
            print('------------')
        # words_list = bag_of_words.extractall_information(globalparameter.folderpath[0]+'/'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,globalparameter.folderpath[0]+'/non_'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,0,
        #     int(globalparameter.extract_number * 0.5), globalparameter.extract_number,
        #     globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * 0.5),globalparameter.extract_column_list)
    #     print(1)
    # for i in range(48):
    #     globalparameter.alg_precision[i] = (globalparameter.alg_precision[i]) / 5
    #     globalparameter.alg_recall[i] = (globalparameter.alg_recall[i]) / 5
    #     globalparameter.alg_accuracy[i] = (globalparameter.alg_accuracy[i]) / 5
    #     globalparameter.time[i] = (globalparameter.time[i]) / 5
    #
    # print('Precision value list: {}'.format(globalparameter.alg_precision))
    # print('Recall value list: {}'.format(globalparameter.alg_recall))
    # print('Accuracy value list: {}'.format(globalparameter.alg_accuracy))
    # result_list = pd.DataFrame({'precision': globalparameter.alg_precision, 'recall': globalparameter.alg_recall,
    #                             'accuracy': globalparameter.alg_accuracy, 'time': globalparameter.time})
    # result_list.to_csv('/Users/pengyuzhou/Google Drive/Linkedin_datafile/all_result_list.csv')
    # print()


if __name__ == '__main__':
    contentbased_old()

    # OO-based method
    # initiate data
    # linkedIndata_list = []
    # with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/data_v3.csv', 'r') as f:
    #     next(f)
    #     reader = csv.reader(f)
    #     for row in reader:
    #         parameter_list = [row[index] for index in range(112)]
    #         linkedIndata_list.append(
    #             linkedindata.LinkedInData(*parameter_list))
    # # extract year by regular expression
    # test_list = calculate_data_job_now.calculate_work_year_oo(linkedIndata_list)
    # length_of_test_set = len(test_list[0])
    # length_of_linkedindata = len(linkedIndata_list)
    # for i in range(len(test_list[0])):
    #     linkedIndata_list[i].getworkdurationvalue(*[test_list[k][i] for k in range(10)])
    # # data filter
    # relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list, globalparameter.jobtitle_list[0],
    #                                                               1)
    # non_relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list,
    #                                                                   globalparameter.jobtitle_list[0], 2)
    # length_relevant_user = len(relevant_user_list)
    # length_non_relevant_user = len(non_relevant_user_list)
    # # iterations for calculate average precision
    # # add code for word embedding
    # pos_list = random.sample(relevant_user_list, 500)
    # neg_list = random.sample(non_relevant_user_list, 500)
    # result = []
    # result_list = []
    # test = relevant_user_list[300].return_value()
    # true_positive = 0
    # filename = '/Users/pengyuzhou/Downloads/GoogleNews-vectors-negative300.bin'
    # model = KeyedVectors.load_word2vec_format(filename, binary=True)
    # for i in range(len(pos_list)):
    #     user_prfile_list_positive = [pos_list[i].past_job_title1.split() + pos_list[i].past_job_org_summary1.split()]
    #     user_prfile_list_negative = [pos_list[i].org_summary.split()]
    #     result = model.most_similar(positive=user_prfile_list_positive,negative=user_prfile_list_negative, topn=6)
    #     for k in range(len(result)):
    #         result_list.append(result[k][0])
    #     if pos_list[i].title in result_list:
    #         true_positive = true_positive+1
    # print(true_positive)
print(1)
