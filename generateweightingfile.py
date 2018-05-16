from sklearn import preprocessing
import pandas as pd
import globalparameter


def generateweighting():
    fields1 = ['id', 'highest_degree']
    fields2 = ['work_year']
    fields3 = ['exp_time']
    fields4 = ['cosine_similarity_value']
    colnames1 = ['id', 'highest_degree']
    colnames2 = ['id', 'work_year']
    colnames3 = ['id', 'exp_time']
    colnames4 = ['id', 'cosine_similarity_value']
    id = []
    highest_degree = []
    work_year = []
    exp_time = []
    cosine_similarity = []
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
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
        names=colnames3, skipinitialspace=True, usecols=fields3)
    exp_time = exp_time + df['exp_time'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title+'cosine_similarity_test.csv',
        names=colnames4, skipinitialspace=True,skiprows=2, usecols=fields4)
    cosine_similarity = cosine_similarity+ df['cosine_similarity_value'].tolist()

    length_id = len(id)
    length_highest_degree = len(highest_degree)
    length_work_year = len(work_year)
    length_exp_time = len(exp_time)
    length_cosine_similarity = len(cosine_similarity)

    frame = pd.DataFrame({'id':id,'highest_degree':highest_degree,'work_year': work_year,'exp_time': exp_time,'cosine_similarity':cosine_similarity})

    frame.to_csv(globalparameter.path+'/test.csv')
