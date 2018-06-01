import pandas as pd
import numpy as np
import globalparameter, extract_multivalue_feature


def generate_X_train(folderpath, jobtitle,X, ratio):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))
    #
    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]
    X_train = pd.concat(
        [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    skill_dummy_array = extract_multivalue_feature.extractskill(
        folderpath + '/' + jobtitle + globalparameter.output_file_root,
        folderpath + '/non_' + jobtitle + globalparameter.output_file_root, ratio, 0,
        int(globalparameter.extract_number * ratio), globalparameter.total_number,
        globalparameter.total_number+int((globalparameter.total_number - globalparameter.extract_number) * ratio))
    xtrain = len(X_train)
    skill_dummy = len(skill_dummy_array)
    X_train.index = range(int(globalparameter.total_number*ratio))
    skill_dummy_array.index = range(int(globalparameter.total_number*ratio))
    new_X_train = X_train

    # new_X_train = pd.concat([X_train, skill_dummy_array],axis=1,join_axes=[X_train.index])
    shape1 = (skill_dummy_array.shape)
    shape2 = new_X_train.shape
    return new_X_train


def generate_X_test(folderpath, jobtitle,X, ratio):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))
    #
    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]
    X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    skill_dummy_array = extract_multivalue_feature.extractskill(
        folderpath + '/' + jobtitle + globalparameter.output_file_root,
        folderpath + '/non_' + jobtitle + globalparameter.output_file_root, ratio,
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number, globalparameter.total_number+int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number+globalparameter.total_number-globalparameter.extract_number)
    xtrain = len(X_test)
    skill_dummy = len(skill_dummy_array)
    X_test.index = range(int(globalparameter.total_number*(1-ratio)))
    skill_dummy_array.index = range(int(globalparameter.total_number*(1-ratio)))
    new_X_test = X_test

    # new_X_test = pd.concat([X_test, skill_dummy_array], axis=1, join_axes=[X_test.index])
    shape1 = (skill_dummy_array.shape)
    shape2 = new_X_test.shape
    return new_X_test
