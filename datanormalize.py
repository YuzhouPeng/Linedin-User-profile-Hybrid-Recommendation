from sklearn import preprocessing
import pandas as pd
import globalparameter

def normalize_highest_degree(input_file_path, output_job_title, name_for_search):
    colnames = ['id',name_for_search]
    fields = ['id', name_for_search]
    df = pd.read_csv(input_file_path,
                     names=colnames,skipinitialspace=True, usecols=fields,header=None)
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
    normalzied_value = pd.DataFrame(x_scaled, columns=['normalized_id', 'normalized_'+name_for_search]).to_csv(
       globalparameter.path+output_job_title+name_for_search+'_normalized'+globalparameter.output_file_root )


def normalize_workyear_exptime(input_file_path, output_job_title, name_for_search):
    colnames = ['id', name_for_search]
    fields = ['id', name_for_search]
    df = pd.read_csv(input_file_path,
                     names=colnames,skipinitialspace=True, usecols=fields,header=None)
    x = df.values  # returns a numpy array
    # iteration of the highest degree
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    # x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
    normalzied_value = pd.DataFrame(x_scaled, columns=['normalized_id', 'normalized_'+name_for_search]).to_csv(
        globalparameter.path+output_job_title+name_for_search+'_normalized'+globalparameter.output_file_root )
