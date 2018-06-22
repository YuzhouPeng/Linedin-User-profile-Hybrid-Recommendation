import pandas as pd
import numpy as np
import globalparameter


# def dummy_filter(dummy_array, threshold, name):


# ratio could be added later


def extractskill(datapath, non_datapath, pos_start_index, pos_end_index, neg_start_index, neg_end_index):
    name = 'skills'
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    # create df data same as train set
    df = pd.concat([user_data.iloc[0:globalparameter.extract_number, [65]],
                    non_user_data.iloc[0:globalparameter.total_number - globalparameter.extract_number,
                    [65]]]).values.tolist()
    user_skill_data = []
    user_skill_data1 = []
    user_skill_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_skill_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_skill_data)):
        user_skill_data1.append(user_skill_data[i].split())
    # print(user_skill_data1)

    user_skill_data1 = pd.DataFrame({'skills': user_skill_data1})
    # print(user_skill_data1)
    length1 = len(user_skill_data1)

    i = 0
    for row in user_skill_data1.iterrows():
        user_skill_data_for_dummy['user_skill' + str(i)] = row[1]
        i = i + 1

    # filtered_skill_variable_array = dummy_filter(pd.DataFrame(user_skill_data1.skills.values.tolist()),0.8,name)

    # dummy_col_list = []
    # test1 = pd.DataFrame(user_skill_data1.skills.values.tolist())
    # dummy_col = pd.DataFrame(user_skill_data1.skills.values.tolist())
    #
    # count_test = dummy_col.count()
    # count = pd.value_counts(dummy_col)/len(dummy_col)
    # mask = dummy_col.isin(count[count>0.8].index)
    # dummy_col[~mask] = "others"
    # filtered_skill_variable_array = pd.get_dummies(dummy_col,prefix=name)

    # test_skill_array = filtered_skill_variable_array

    # print(user_skill_data_for_dummy)
    skill_variable_array = pd.get_dummies(pd.DataFrame(user_skill_data1.skills.values.tolist()), drop_first=True)
    new_skill_variable_array = pd.concat([skill_variable_array.iloc[pos_start_index:pos_end_index],
                                          skill_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_skill_variable_array)
    print(skill_variable_array.shape)
    return new_skill_variable_array


def extractschool(datapath, non_datapath, pos_start_index, pos_end_index, neg_start_index, neg_end_index):
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    df = pd.concat([user_data.iloc[:, [45]],
                    non_user_data.iloc[:, [45]]]).values.tolist()
    user_school_data = []
    user_school_data1 = []
    user_school_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_school_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_school_data)):
        user_school_data1.append(user_school_data[i].split())
    # print(user_skill_data1)

    user_school_data1 = pd.DataFrame({'schools': user_school_data1})
    # print(user_skill_data1)
    length1 = len(user_school_data1)

    i = 0
    for row in user_school_data1.iterrows():
        user_school_data_for_dummy['user_school' + str(i)] = row[1]
        i = i + 1

    # print(user_school_data_for_dummy)
    school_variable_array = pd.get_dummies(pd.DataFrame(user_school_data1.schools.values.tolist()), drop_first=True)
    new_school_variable_array = pd.concat([school_variable_array.iloc[pos_start_index:pos_end_index],
                                           school_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_school_variable_array)
    print(school_variable_array.shape)
    return new_school_variable_array


def extractmajor(datapath, non_datapath, pos_start_index, pos_end_index, neg_start_index, neg_end_index):
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)

    df = pd.concat([user_data.iloc[:, [47]],
                    non_user_data.iloc[:, [47]]]).values.tolist()
    user_major_data = []
    user_major_data1 = []
    user_major_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_major_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_major_data)):
        user_major_data1.append(user_major_data[i].split())
    # print(user_skill_data1)

    user_major_data1 = pd.DataFrame({'schools': user_major_data1})
    # print(user_skill_data1)
    length1 = len(user_major_data1)

    i = 0
    for row in user_major_data1.iterrows():
        user_major_data_for_dummy['user_school' + str(i)] = row[1]
        i = i + 1

    # print(user_major_data_for_dummy)
    major_variable_array = pd.get_dummies(pd.DataFrame(user_major_data1.schools.values.tolist()), drop_first=True)
    new_major_variable_array = pd.concat([major_variable_array.iloc[pos_start_index:pos_end_index],
                                          major_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_major_variable_array)
    print(major_variable_array.shape)
    return new_major_variable_array


def extractworkcompany(datapath, non_datapath, pos_start_index, pos_end_index, neg_start_index, neg_end_index,
                       column_index):
    # now work company index = [4], past work company index = [10,16,22,28,34,40]
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    df = pd.concat([user_data.iloc[:, [column_index]],
                    non_user_data.iloc[:, [column_index]]]).values.tolist()
    user_company_data = []
    user_company_data1 = []
    user_company_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_company_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_company_data)):
        user_company_data1.append(user_company_data[i].split())
    # print(user_skill_data1)

    user_company_data1 = pd.DataFrame({'companies': user_company_data1})
    # print(user_skill_data1)
    length1 = len(user_company_data1)

    i = 0
    for row in user_company_data1.iterrows():
        user_company_data_for_dummy['user_company' + str(i)] = row[1]
        i = i + 1

    # print(user_company_data_for_dummy)
    company_variable_array = pd.get_dummies(pd.DataFrame(user_company_data1.companies.values.tolist()), drop_first=True)
    new_company_variable_array = pd.concat([company_variable_array.iloc[pos_start_index:pos_end_index],
                                            company_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_company_variable_array)
    print(company_variable_array.shape)
    return new_company_variable_array


