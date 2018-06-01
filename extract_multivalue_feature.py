import pandas as pd
import numpy as np
import globalparameter


def extractskill(datapath, non_datapath, ratio,pos_start_index,pos_end_index,neg_start_index,neg_end_index):
    user_data = pd.DataFrame(pd.read_csv(datapath))
    non_user_data = pd.DataFrame(pd.read_csv(non_datapath))
    # create df data same as train set
    df = pd.concat([user_data.iloc[0:globalparameter.total_number, [65]],
                    non_user_data.iloc[0:globalparameter.total_number, [65]]]).values.tolist()
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
        user_skill_data_for_dummy['user' + str(i)] = row[1]
        i = i + 1

    # print(user_skill_data_for_dummy)
    skill_variable_array = pd.get_dummies(pd.DataFrame(user_skill_data1.skills.values.tolist()))
    new_skill_variable_array = pd.concat([skill_variable_array.iloc[pos_start_index:pos_end_index],
                                         skill_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_skill_variable_array)
    print(skill_variable_array.shape)
    return new_skill_variable_array


def extractschool(folderpath):
    user_data = pd.DataFrame(pd.read_csv(
        '/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer/software_engineer_lowercase_no_punctuation.csv'))
    df = user_data.iloc[:, [45]].values.tolist()
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

    user_school_data1 = pd.DataFrame({'skills': user_school_data1})
    # print(user_skill_data1)
    length1 = len(user_school_data1)

    i = 0
    for row in user_school_data1.iterrows():
        user_school_data_for_dummy['user' + str(i)] = row[1]
        i = i + 1

    print(user_school_data_for_dummy)
    skill_variable_array = pd.get_dummies(pd.DataFrame(user_school_data1.skills.values.tolist()))
    print(skill_variable_array.shape)


def extractmajor(folderpath):
    user_data = pd.DataFrame(pd.read_csv(
        '/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer/software_engineer_lowercase_no_punctuation.csv'))
    df = user_data.iloc[:, [47]].values.tolist()
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

    user_major_data1 = pd.DataFrame({'skills': user_major_data1})
    # print(user_skill_data1)
    length1 = len(user_major_data1)

    i = 0
    for row in user_major_data1.iterrows():
        user_major_data_for_dummy['user' + str(i)] = row[1]
        i = i + 1

    print(user_major_data_for_dummy)
    skill_variable_array = pd.get_dummies(pd.DataFrame(user_major_data1.skills.values.tolist()))
    print(skill_variable_array.shape)


def extractworkcompany(folderpath):
    # now work company index = [4], past work company index = [10,16,22,28,34,40]
    user_data = pd.DataFrame(pd.read_csv(
        '/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer/software_engineer_lowercase_no_punctuation.csv'))
    df = user_data.iloc[:, [10]].values.tolist()
    user_workcompany_data = []
    user_workcompany_data1 = []
    user_workcompany_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_workcompany_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_workcompany_data)):
        user_workcompany_data1.append(user_workcompany_data[i].split())
    # print(user_skill_data1)

    user_workcompany_data1 = pd.DataFrame({'skills': user_workcompany_data1})
    # print(user_skill_data1)
    length1 = len(user_workcompany_data1)

    i = 0
    for row in user_workcompany_data1.iterrows():
        user_workcompany_data_for_dummy['user' + str(i)] = row[1]
        i = i + 1

    print(user_workcompany_data_for_dummy)
    skill_variable_array = pd.get_dummies(pd.DataFrame(user_workcompany_data1.skills.values.tolist()))
    print(skill_variable_array.shape)
