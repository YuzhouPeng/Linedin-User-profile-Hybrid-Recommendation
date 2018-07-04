from sklearn import preprocessing
import pandas as pd
import globalparameter, csv, random


def generateweighting_expect_newest(number_of_extract, folderpath, jobtitle_path_list):
    fields1 = ['id']
    fields2 = ['work_year_past1', 'work_year_past2', 'work_year_past3', 'work_year_past4', 'work_year_past5',
               'work_year_past6']

    colnames1 = ['id']
    colnames2 = ['id', 'work_year_past1', 'work_year_past2', 'work_year_past3', 'work_year_past4', 'work_year_past5',
                 'work_year_past6']

    id = []
    work_year_past1 = []
    work_year_past2 = []
    work_year_past3 = []
    work_year_past4 = []
    work_year_past5 = []
    work_year_past6 = []
    exp_time = []
    now_relevant_job = []
    now_relevant_job = now_relevant_job + [1] * number_of_extract + [0] * (
            globalparameter.total_number - number_of_extract)
    # cosine_similarity = []
    df = pd.read_csv(
        folderpath + '/' + jobtitle_path_list + '_' + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    id = id + (df['id'].tolist())
    positive_sample_id = id
    # calculate positive id index
    positive_random_id_list = random.sample(id, globalparameter.extract_number)
    positive_random_index_list = []
    for i in range(len(positive_random_id_list)):
        for j in range(len(id)):
            if positive_random_id_list[i] == id[j]:
                positive_random_index_list.append(j)
    id = positive_random_id_list

    df = pd.read_csv(
        folderpath + '/' + jobtitle_path_list + '_' + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    for i in range(len(positive_random_index_list)):
        work_year_past1 = work_year_past1 + [(df['work_year_past1'].tolist())[positive_random_index_list[i]]]
        work_year_past2 = work_year_past2 + [(df['work_year_past2'].tolist())[positive_random_index_list[i]]]
        work_year_past3 = work_year_past3 + [(df['work_year_past3'].tolist())[positive_random_index_list[i]]]
        work_year_past4 = work_year_past4 + [(df['work_year_past4'].tolist())[positive_random_index_list[i]]]
        work_year_past5 = work_year_past5 + [(df['work_year_past5'].tolist())[positive_random_index_list[i]]]
        work_year_past6 = work_year_past6 + [(df['work_year_past6'].tolist())[positive_random_index_list[i]]]

    df = pd.read_csv(
        folderpath + '/non_' + jobtitle_path_list + '_' + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    random_id_list = random.sample(df['id'].tolist(), globalparameter.total_number - globalparameter.extract_number)
    # calculate negative id index
    id_list = df['id'].tolist()
    random_index_list = []
    id = id + (random_id_list)
    id_list_test = df['id'].tolist()
    for i in range(len(random_id_list)):
        for j in range(len(id_list)):
            if random_id_list[i] == id_list[j]:
                random_index_list.append(j)

    df = pd.read_csv(
        folderpath + '/non_' + jobtitle_path_list + '_' + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    for i in range(len(random_index_list)):
        work_year_past1 = work_year_past1 + [(df['work_year_past1'].tolist())[random_index_list[i]]]
        work_year_past2 = work_year_past2 + [(df['work_year_past2'].tolist())[random_index_list[i]]]
        work_year_past3 = work_year_past3 + [(df['work_year_past3'].tolist())[random_index_list[i]]]
        work_year_past4 = work_year_past4 + [(df['work_year_past4'].tolist())[random_index_list[i]]]
        work_year_past5 = work_year_past5 + [(df['work_year_past5'].tolist())[random_index_list[i]]]
        work_year_past6 = work_year_past6 + [(df['work_year_past6'].tolist())[random_index_list[i]]]

    length_id = len(id)
    length_exp_time = len(exp_time)
    # length_cosine_similarity = len(cosine_similarity)
    length_work_year1 = len(work_year_past1)
    length_work_year2 = len(work_year_past2)
    length_now_job = len(now_relevant_job)

    list_for_iterate = []
    writer = csv.writer(open(folderpath + '/' + 'output_neg_for_dummy.csv', 'w'))
    with open(globalparameter.raw_data_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            list_for_iterate.append(row)
        for i in range(len(random_id_list)):
            for j in range(len(list_for_iterate)):
                if str(random_id_list[i]) == list_for_iterate[j][0]:
                    writer.writerow(list_for_iterate[j])
    list_for_iterate = []
    writer1 = csv.writer(open(folderpath + '/' + 'output_pos_for_dummy.csv', 'w'))
    with open(globalparameter.raw_data_path, 'r') as f:
        reader1 = csv.reader(f)
        for row in reader1:
            list_for_iterate.append(row)
        for i in range(len(positive_random_id_list)):
            for j in range(len(list_for_iterate)):
                if str(positive_random_id_list[i]) == list_for_iterate[j][0]:
                    writer1.writerow(list_for_iterate[j])

    random_id_list_data = pd.DataFrame({'data_id': random_id_list})
    random_id_list_data.to_csv(folderpath + '/' + 'output_id_data.csv')
    len_work_year_past1 = len(work_year_past1)
    len_work_year_past2 = len(work_year_past2)
    len_work_year_past3 = len(work_year_past3)
    len_work_year_past4 = len(work_year_past4)
    len_work_year_past5 = len(work_year_past5)
    len_work_year_past6 = len(work_year_past6)
    len_relevant_job = len(now_relevant_job)

    frame = pd.DataFrame({'id': id, 'work_year_past1': work_year_past1,
                          'work_year_past2': work_year_past2, 'work_year_past3': work_year_past3,
                          'work_year_past4': work_year_past4, 'work_year_past5': work_year_past5,
                          'work_year_past6': work_year_past6,
                          'now_relevant_job': now_relevant_job})

    frame.to_csv(folderpath + '/test.csv')
