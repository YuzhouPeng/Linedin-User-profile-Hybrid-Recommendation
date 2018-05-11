from sklearn import preprocessing
import pandas as pd
import globalparameter


def generateweighting():
    fields1 = ['id', 'highest_degree']
    fields2 = ['work_year']
    fields3 = ['exp_time']
    colnames1 = ['id', 'highest_degree']
    colnames2 = ['id', 'work_year']
    colnames3 = ['id', 'exp_time']
    id = []
    highest_degree = []
    work_year = []
    exp_time = []
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    id = id+(df['id'].tolist())
    highest_degree = highest_degree+ df['highest_degree'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    id = id+(df['id'].tolist())
    highest_degree = highest_degree+ df['highest_degree'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year = work_year+df['work_year'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year = work_year+df['work_year'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
        names=colnames3, skipinitialspace=True, usecols=fields3)
    exp_time = exp_time + df['exp_time'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
        names=colnames3, skipinitialspace=True, usecols=fields3)
    exp_time = exp_time + df['exp_time'].tolist()
    frame = pd.DataFrame({'id':id,'highest_degree':highest_degree,'work_year': work_year,'exp_time': exp_time})

    frame.to_csv('/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer/test.csv')
