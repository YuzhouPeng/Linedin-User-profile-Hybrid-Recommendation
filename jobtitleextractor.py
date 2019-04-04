import csv, globalparameter
import pandas as pd
# for i in range(6):
def extract_jobtitle(index):
    job_title_list = []
    pos_data_path = globalparameter.folderpath[index] + '/' + 'output_pos_for_dummy.csv'
    neg_data_path = globalparameter.folderpath[index] + '/' + 'output_neg_for_dummy.csv'
    csv_file_pos = csv.reader(open(pos_data_path, "r"))
    csv_file_neg = csv.reader(open(neg_data_path, "r"))
    # index:
    index_list  = [3,9,15,21,27,33,39]
    for row in csv_file_pos:
        for k in range(len(index_list)):
            if row[index_list[k]]:
                job_title_list.append(row[index_list[k]])
    for row in csv_file_neg:
        for k in range(len(index_list)):
            if row[index_list[k]]:
                job_title_list.append(row[index_list[k]])

    job_title_list = list(set(job_title_list))
    print(1)
    return job_title_list