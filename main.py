import datanormalize, generateweightingfile, \
    datafilter, calculate_data_job_now, alg_logestic_regression, alg_svm, \
    alg_bayes, alg_decision_tree, alg_ramdom_forest, extract_multivalue_feature, generate_train_test_set, \
    calculate_baseline, bag_of_words
import globalparameter, csv, linkedindata, random
import time
import pandas as pd


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
        # normalizing_data()
        j = 0
        for i in range(6):
            print('------job title is:------')
            print(globalparameter.jobtitle_path_list[i])
            # print('baseline precision value of job title is: ')
            #     calculate_baseline.baseline_full_text(globalparameter.jobtitle_list[i],globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
            #                                                globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
            #     calculate_baseline.baseline_work_exp(globalparameter.jobtitle_list[i],globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
            #                                                globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv')
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


if __name__ == '__main__':
    # contentbased_old()

    # OO-based method
    # initiate data
    linkedIndata_list = []
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
    # data filter
    relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list, globalparameter.jobtitle_list[0],
                                                                  1)
    non_relevant_user_list = datafilter.filter_data_with_job_title_oo(linkedIndata_list,
                                                                      globalparameter.jobtitle_list[0], 2)
    length_relevant_user = len(relevant_user_list)
    length_non_relevant_user = len(non_relevant_user_list)
    work_experience_effective_value_list = [0] * 11
    work_experience_total_work_year = 0.0
    edu_background_effect_value_list = [0] * 8
    skill_number = 0

    for i in range(len(linkedIndata_list)):
        if linkedIndata_list[i].title:
            work_experience_effective_value_list[0] = work_experience_effective_value_list[0] + 1
        if linkedIndata_list[i].past_job_title1:
            work_experience_effective_value_list[1] = work_experience_effective_value_list[1] + 1
        if linkedIndata_list[i].past_job_title2:
            work_experience_effective_value_list[2] = work_experience_effective_value_list[2] + 1
        if linkedIndata_list[i].past_job_title3:
            work_experience_effective_value_list[3] = work_experience_effective_value_list[3] + 1
        if linkedIndata_list[i].past_job_title4:
            work_experience_effective_value_list[4] = work_experience_effective_value_list[4] + 1
        if linkedIndata_list[i].past_job_title5:
            work_experience_effective_value_list[5] = work_experience_effective_value_list[5] + 1
        if linkedIndata_list[i].past_job_title6:
            work_experience_effective_value_list[6] = work_experience_effective_value_list[6] + 1
        if linkedIndata_list[i].past_job_title7:
            work_experience_effective_value_list[7] = work_experience_effective_value_list[7] + 1
        if linkedIndata_list[i].past_job_title8:
            work_experience_effective_value_list[8] = work_experience_effective_value_list[8] + 1
        if linkedIndata_list[i].past_job_title9:
            work_experience_effective_value_list[9] = work_experience_effective_value_list[9] + 1
        if linkedIndata_list[i].past_job_title10:
            work_experience_effective_value_list[10] = work_experience_effective_value_list[10] + 1
        work_experience_total_work_year = work_experience_total_work_year + linkedIndata_list[i].past_job_duration1 + \
                                          linkedIndata_list[i].past_job_duration2 + linkedIndata_list[
                                              i].past_job_duration3 + linkedIndata_list[i].past_job_duration4 + \
                                          linkedIndata_list[i].past_job_duration5 + linkedIndata_list[
                                              i].past_job_duration6 + linkedIndata_list[i].past_job_duration7 + \
                                          linkedIndata_list[i].past_job_duration8 + linkedIndata_list[
                                              i].past_job_duration9 + linkedIndata_list[i].past_job_duration10
        if linkedIndata_list[i].highestLevel_universityName:
            edu_background_effect_value_list[0] = edu_background_effect_value_list[0] + 1
        if linkedIndata_list[i].otherLevel_universityName1:
            edu_background_effect_value_list[1] = edu_background_effect_value_list[1] + 1
        if linkedIndata_list[i].otherLevel_universityName2:
            edu_background_effect_value_list[2] = edu_background_effect_value_list[2] + 1
        if linkedIndata_list[i].otherLevel_universityName3:
            edu_background_effect_value_list[3] = edu_background_effect_value_list[3] + 1
        if linkedIndata_list[i].otherLevel_universityName4:
            edu_background_effect_value_list[4] = edu_background_effect_value_list[4] + 1
        if linkedIndata_list[i].otherLevel_universityName5:
            edu_background_effect_value_list[5] = edu_background_effect_value_list[5] + 1
        if linkedIndata_list[i].otherLevel_universityName6:
            edu_background_effect_value_list[6] = edu_background_effect_value_list[6] + 1
        if linkedIndata_list[i].otherLevel_universityName7:
            edu_background_effect_value_list[7] = edu_background_effect_value_list[7] + 1
        skill_list = linkedIndata_list[i].skills.split(',')
        skill_number = skill_number+ len(skill_list)


    # iterations for calculate average precision
    pos_list = random.sample(relevant_user_list, 500)
    neg_list = random.sample(non_relevant_user_list, 500)
    test = relevant_user_list[300].return_value()

    print(1)
