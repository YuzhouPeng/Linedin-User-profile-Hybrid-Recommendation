import pandas as pd
import csv
from numpy import random
from sklearn.metrics import precision_score


def baseline_full_text():
    name = 'project manager'
    list_rev = []
    list_rev_column = []
    list_non_rev = []
    list_non_rev_column = []
    bool_list_baseline = []
    bool_list = []
    bool_non_list = []
    with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = ' '.join(row)
            if name in new_row:
                list_rev.append(new_row)
                list_rev_column.append(list(row[i] for i in range(len(row))))
            else:
                list_non_rev.append(new_row)
                # list_non_rev_column.append(list(row[i] for i in row))


    random_non_list = random.choice(list_non_rev,500)

    for i in range(0,500):
        if name in list_rev[i]:
            bool_list_baseline.append(1)
        else:
            bool_list_baseline.append(0)
    for i in range(0,500):
        if name in list_rev_column[i][3]:
            bool_list.append(1)
        else:
            bool_list.append(0)
    for i in range(len(random_non_list)):
        if name in random_non_list[i]:
            bool_non_list.append(1)
        else:
            bool_non_list.append(0)

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

    score = precision_score(bool_list+zero_list, bool_list_baseline+bool_non_list)
    print(score)


# def baseline_work_exp():
name = 'project manager'
list_rev = []
list_rev_column = []
list_non_rev = []
list_non_rev_column = []
bool_list_baseline = []
bool_list = []
bool_non_list = []
with open('/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        new_row = ' '.join(row[5:44])
        if name in new_row:
            list_rev.append(new_row)
            list_rev_column.append(list(row[i] for i in range(len(row))))
        else:
            list_non_rev.append(new_row)
            # list_non_rev_column.append(list(row[i] for i in row))

random_non_list = random.choice(list_non_rev, 500)

for i in range(0, 500):
    if name in list_rev[i]:
        bool_list_baseline.append(1)
    else:
        bool_list_baseline.append(0)
for i in range(0, 500):
    if name in list_rev_column[i][3]:
        bool_list.append(1)
    else:
        bool_list.append(0)
for i in range(len(random_non_list)):
    if name in random_non_list[i]:
        bool_non_list.append(1)
    else:
        bool_non_list.append(0)

zero_list = [0] * 500


score = precision_score(bool_list + zero_list, bool_list_baseline + bool_non_list)
print(score)