from sklearn import preprocessing
from sklearn.preprocessing import normalize
import pandas as pd
import globalparameter


def normalize_highest_degree(input_file_path, output_job_title, name_for_search):
    colnames = ['id', name_for_search]
    fields = ['id', name_for_search]
    df = pd.read_csv(input_file_path,
                     names=colnames, skipinitialspace=True, usecols=fields, header=None)
    x = df.values  # returns a numpy array
    degree = []
    # iteration of the highest degree
    for row in df[name_for_search]:
        if row == 1:
            degree.append(3)
        elif row >= 2 and row <= 4:
            degree.append(2)
        elif row >= 5 and row <= 7:
            degree.append(1)
        else:
            degree.append(0)

    degree = pd.DataFrame(degree, columns=[name_for_search])
    df[name_for_search] = degree[name_for_search]
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(df)
    # x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
    normalzied_value = pd.DataFrame(x_scaled, columns=['normalized_id', 'normalized_' + name_for_search]).to_csv(
        globalparameter.path + output_job_title + name_for_search + '_normalized' + globalparameter.output_file_root)


def normalize_workyear_exptime(input_file_path, output_job_title, name_for_search):
    colnames = ['id', name_for_search]
    fields = ['id', name_for_search]
    df = pd.read_csv(input_file_path,
                     names=colnames, skipinitialspace=True, usecols=fields, header=None)
    x = df.values  # returns a numpy array
    # iteration of the highest degree
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    # x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
    normalzied_value = pd.DataFrame(x_scaled, columns=['normalized_id', 'normalized_' + name_for_search]).to_csv(
        globalparameter.path + output_job_title + name_for_search + '_normalized' + globalparameter.output_file_root)


def normalize_weighting_highest_degree(input_file_path, folderpath):
    # colnames = ['id',name_for_search]
    fields = ['rowindex', 'id', 'now_relevant_job', 'work_year_past1', 'work_year_past2',
              'work_year_past3', 'work_year_past4', 'work_year_past5', 'work_year_past6']
    df = pd.read_csv(input_file_path,
                     names=fields, skipinitialspace=True, usecols=fields, skiprows=1)
    x = df.values  # returns a numpy array
    # iteration of the highest degree

    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled_highest_degree = min_max_scaler.fit_transform(df)
    # x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
    normalzied_value = pd.DataFrame(x_scaled_highest_degree,
                                    columns=['index_normalized', 'normalized_id',
                                             'normalized_now_relevant_job', 'normalized_work_year_past1',
                                             'normalized_work_year_past2', 'normalized_work_year_past3',
                                             'normalized_work_year_past4', 'normalized_work_year_past5',
                                             'normalized_work_year_past6']).to_csv(
        folderpath + '/test1.csv')

    # colnames = ['id', 'work_year']
    # fields = ['id', 'work_year']
    # df = pd.read_csv(input_file_path,
    #                  names=colnames,skipinitialspace=True, usecols=fields,header=None)
    # x = df.values  # returns a numpy array
    # # iteration of the highest degree
    # min_max_scaler = preprocessing.MinMaxScaler()
    # x_scaled = min_max_scaler.fit_transform(x)
    # # x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
    #
    # pd.DataFrame({'id': id, ['normalized_id', 'normalized_highest_degree']: x_scaled})

def normalizingdata_oo(pos_data,neg_data,index):
    normalizingdata_list = []
    for i in range(len(pos_data)):
        normalizingdata_list.append(pos_data[i].past_work_duration_value())
    for i in range(len(neg_data)):
        normalizingdata_list.append(neg_data[i].past_work_duration_value())
    new_normalizingdata_list = normalize(normalizingdata_list,axis=0)
    print(1)
    if index == 1:
        for i in range(500):
            pos_data[i].getworkdurationvalue(*[new_normalizingdata_list[k][i] for k in range(10)])
        return pos_data
    if index == 2:
        for i in range(500):
            neg_data[i].getworkdurationvalue(*[new_normalizingdata_list[j][500+i] for j in range(10)])
        return neg_data
