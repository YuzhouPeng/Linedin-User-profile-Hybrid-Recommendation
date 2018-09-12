import pandas as pd
import globalparameter, extract_multivalue_feature
import collections, string
from sklearn.decomposition import TruncatedSVD


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def extractall_information(datapath, non_datapath, column_index_list):
    # extract columns:[3-5,9-11,15-17,21-23,27-29,33-35,39-41]
    # education:[45-65 length5][46-47,49,51-52,54,56-57,59,61-62,64]
    # skill language:[65,66]
    # -1
    # can not extract column: [7,13,19,25,31,37,43]
    # work year column: []
    # year column: [49,54,59,64]
    # school column: [46,51,56,61]
    # total column number: 67
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    all_info_list = []
    user_data = user_data.fillna("")
    non_user_data = non_user_data.fillna("")
    for i in range(len(column_index_list)):
        column_index = column_index_list[i]
        df = pd.concat([user_data.iloc[:, [column_index]],
                        non_user_data.iloc[:, [column_index]]]).values.tolist()
        all_info_list.append(df)

    user_data = []
    for j in range(1000):
        user_row = []
        for i in range(len(all_info_list)):
            user_row.append(all_info_list[i][j])
        user_data.append(user_row)
    user_total_info_data = []
    user_total_words_info_data1 = []
    user_company_data_for_dummy = pd.DataFrame()

    for i in range(len(user_data)):
        user_data[i] = flatten(user_data[i])
    # print(df)
    for i in range(len(user_data)):
        user_total_info_data.append(' '.join(str(k) for k in user_data[i]))
    # print(user_skill_data)

    # #remove all numerical number
    for i in range(len(user_total_info_data)):
        user_total_info_data[i] = ''.join([x for x in user_total_info_data[i] if not x.isdigit()])

    for i in range(len(user_total_info_data)):
        user_total_words_info_data1.append(user_total_info_data[i].split())
    # print(user_skill_data1)

    user_total_words_info_data1 = pd.DataFrame({'all_data': user_total_words_info_data1})
    # print(user_skill_data1)
    length1 = len(user_total_words_info_data1)

    i = 0
    new_user_total_words_info_data1 = []
    # for i in range(len(user_total_words_info_data1)):
    #     new_user_total_words_info_data1.append([x for x in user_total_words_info_data1[i] if x != 'nan'])

    # print(user_company_data_for_dummy)
    total_words_variable_array = pd.get_dummies(pd.DataFrame(user_total_words_info_data1.all_data.values.tolist()),
                                                drop_first=True)

    # reduce dimention using svd
    svd = TruncatedSVD(50)
    total_words_transformed = svd.fit_transform(total_words_variable_array)
    column_names = ['column_' + str(i) for i in range(50)]
    total_words_transformed = pd.DataFrame(total_words_transformed, columns=column_names)
    # print(total_words_transformed.shape)
    print(total_words_transformed.shape)

    return total_words_transformed


def bag_of_words_generate_X_train(dummy_matrix, X, ratio, pos_start_index, pos_end_index, neg_start_index,
                                  neg_end_index):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))

    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]

    # X = X['normalized_highest_degree']

    X = X[['normalized_work_year_past1', 'normalized_work_year_past2',
           'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
           'normalized_work_year_past6']]

    X_train = pd.concat(
        [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])

    new_dummy_variable_array = pd.concat([dummy_matrix.iloc[pos_start_index:pos_end_index],
                                          dummy_matrix.iloc[neg_start_index:neg_end_index]])

    # Reset the index to make sure the sequence of concat data is right
    X_train.index = range(int(globalparameter.total_number * ratio))
    new_dummy_variable_array.index = range(int(globalparameter.total_number * ratio))

    # new_X_train = X_train
    new_X_train = pd.concat([X_train, new_dummy_variable_array], axis=1, join_axes=[X_train.index])
    # new_X_train = pd.concat([X_train, workcompany_dummy_array1, workcompany_dummy_array2, workcompany_dummy_array3,
    #                          workcompany_dummy_array4, workcompany_dummy_array5, workcompany_dummy_array6], axis=1,
    #                         join_axes=[X_train.index])

    shape2 = new_X_train.shape
    return new_X_train


def bag_of_words_generate_X_test(dummy_matrix, X, ratio, pos_start_index, pos_end_index, neg_start_index,
                                 neg_end_index):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))

    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]

    # X = X['normalized_highest_degree']

    X = X[['normalized_work_year_past1', 'normalized_work_year_past2',
           'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
           'normalized_work_year_past6']]

    X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])

    new_dummy_variable_array = pd.concat([dummy_matrix.iloc[pos_start_index:pos_end_index],
                                          dummy_matrix.iloc[neg_start_index:neg_end_index]])

    # Reset the index to make sure the sequence of concat data is right
    X_test.index = range(int(globalparameter.total_number * (1 - ratio)))

    new_dummy_variable_array.index = range(int(globalparameter.total_number * (1 - ratio)))
    # new_X_test = X_test
    new_X_test = pd.concat([X_test, new_dummy_variable_array], axis=1, join_axes=[X_test.index])
    # new_X_test = pd.concat(
    #     [X_test, workcompany_dummy_array1, workcompany_dummy_array2, workcompany_dummy_array3, workcompany_dummy_array4,
    #      workcompany_dummy_array5, workcompany_dummy_array6], axis=1, join_axes=[X_test.index])
    shape2 = new_X_test.shape
    return new_X_test


def extract_information_oo(classlist):
    list_data = []
    for i in range(len(classlist)):
        # adding work experience information of users
        user_title_data_list = classlist[i].past_job_title1.split(',') + classlist[i].past_job_title2.split(',') + \
                               classlist[
                                   i].past_job_title3.split(',') + classlist[i].past_job_title4.split(',') + classlist[
                                   i].past_job_title5.split(',') + classlist[
                                   i].past_job_title6.split(',')
        new_user_title_data_list = ' '.join(user_title_data_list)

        # adding education background of users
        # adding skill information of users
        test1 = classlist[i].skills
        # data cleaning of the skills
        userskill_data_list = classlist[i].skills.split(',')
        new_final_user_skill_data_list = ' '.join(userskill_data_list)
        final_user_skill_data_list1 = new_final_user_skill_data_list.split(' ')
        final_work_experience_data_list = new_user_title_data_list.split(' ')
        # final user data list
        final_user_data_list = final_user_skill_data_list1+final_work_experience_data_list
        # #remove all numerical number
        for i in range(len(final_user_data_list)):
            final_user_data_list[i] = ''.join([x for x in final_user_data_list[i] if not x.isdigit()])
        list_data.append(final_user_data_list)

    return list_data
