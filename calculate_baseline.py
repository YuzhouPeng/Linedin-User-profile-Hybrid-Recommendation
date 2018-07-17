import pandas as pd
import csv, globalparameter
from numpy import random
from sklearn.metrics import precision_score


def baseline_full_text(name,folderpath_pos,folderpath_neg):
    pos_list = []
    neg_list = []
    with open(folderpath_pos) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row[6:66])
            if name in new_row:
                pos_list.append(1)
            else:
                pos_list.append(0)
                # list_non_rev_column.append(list(row[i
    with open(folderpath_neg) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row)
            if name in new_row:
                neg_list.append(1)
            else:
                neg_list.append(0)
                # list_non_rev_column.append(list(row[i] for i in row))

    bool_list  = [1]*500

    zero_list = [0]*500

    # user_data = pd.read_csv(
    #     '/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv')
    #
    # with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         if name in row[4]:
    #             bool_list.append(1)
    #         else:
    #             bool_list.append(0)

    score = precision_score(bool_list+zero_list, pos_list+neg_list)
    print('baseline_precision_full_text_of '+name+' : {}'.format(score))


def baseline_work_exp(name,folderpath_pos,folderpath_neg):

    pos_list = []
    neg_list = []
    with open(folderpath_pos) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row[9:44])
            if name in new_row:
                pos_list.append(1)
            else:
                pos_list.append(0)
                # list_non_rev_column.append(list(row[i
    with open(folderpath_neg) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row[5:44])
            if name in new_row:
                neg_list.append(1)
            else:
                neg_list.append(0)
                # list_non_rev_column.append(list(row[i] for i in row))

    bool_list  = [1]*500

    zero_list = [0]*500

    # user_data = pd.read_csv(
    #     '/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv')
    #
    # with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         if name in row[4]:
    #             bool_list.append(1)
    #         else:
    #             bool_list.append(0)

    score = precision_score(bool_list+zero_list, pos_list+neg_list)
    print('baseline_precision_full_text_of '+name+' : {}'.format(score))