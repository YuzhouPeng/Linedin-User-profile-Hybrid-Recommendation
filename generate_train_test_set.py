import pandas as pd
import numpy as np
import globalparameter, extract_multivalue_feature


def generate_X_train(dummy_matrix, X, ratio, pos_start_index, pos_end_index, neg_start_index, neg_end_index):
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


def generate_X_test(dummy_matrix, X, ratio, pos_start_index, pos_end_index, neg_start_index, neg_end_index):
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


def generate_train_test_oo(pos_data, neg_data, pos_train_start, pos_train_end, pos_test_start, pos_test_end,
                           neg_train_start, neg_train_end, neg_test_start, neg_test_end):
    return