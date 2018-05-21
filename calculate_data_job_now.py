import globalparameter, itertools, csv, re
import pandas as pd


def calculate_work_year_except_newest(path, job_title_name, job_title_data_path, extract_number):
    with open(
            job_title_data_path,
            'r') as csvfile:
        name = job_title_name
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(
            open(
                path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
                'w'))
        for row in itertools.islice(reader, extract_number):
            # print(i)
            work_experience_total_year_past1 = 0
            work_experience_total_month_past1 = 0
            work_experience_total_year_past2 = 0
            work_experience_total_month_past2 = 0
            work_experience_total_year_past3 = 0
            work_experience_total_month_past3 = 0
            work_experience_total_year_past4 = 0
            work_experience_total_month_past4 = 0
            work_experience_total_year_past5 = 0
            work_experience_total_month_past5 = 0
            work_experience_total_year_past6 = 0
            work_experience_total_month_past6 = 0
            work_year_past1 = 0
            work_year_past2 = 0
            work_year_past3 = 0
            work_year_past4 = 0
            work_year_past5 = 0
            work_year_past6 = 0

            if (row[9].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[12])
                m_year = regex_year.findall(row[12])
                m_month = regex_month.findall(row[12])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past1 = work_experience_total_year_past1 + str_year_num
                work_experience_total_month_past1 = work_experience_total_month_past1 + str_month_num
                work_year_past1 = float(work_experience_total_year_past1) + (
                        float(work_experience_total_month_past1) / 12.00)

            if (row[15].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[18])
                m_year = regex_year.findall(row[18])
                m_month = regex_month.findall(row[18])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past2 = work_experience_total_year_past2 + str_year_num
                work_experience_total_month_past2 = work_experience_total_month_past2 + str_month_num
                work_year_past2 = float(work_experience_total_year_past2) + (
                        float(work_experience_total_month_past2) / 12.00)

            if (row[21].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[24])
                m_year = regex_year.findall(row[24])
                m_month = regex_month.findall(row[24])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past3 = work_experience_total_year_past3 + str_year_num
                work_experience_total_month_past3 = work_experience_total_month_past3 + str_month_num
                work_year_past3 = float(work_experience_total_year_past3) + (
                        float(work_experience_total_month_past3) / 12.00)

            if (row[27].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[30])
                m_year = regex_year.findall(row[30])
                m_month = regex_month.findall(row[30])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past4 = work_experience_total_year_past4 + str_year_num
                work_experience_total_month_past4 = work_experience_total_month_past4 + str_month_num
                work_year_past4 = float(work_experience_total_year_past4) + (
                        float(work_experience_total_month_past4) / 12.00)

            if (row[33].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[36])
                m_year = regex_year.findall(row[36])
                m_month = regex_month.findall(row[36])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past5 = work_experience_total_year_past5 + str_year_num
                work_experience_total_month_past5 = work_experience_total_month_past5 + str_month_num
                work_year_past5 = float(work_experience_total_year_past5) + (
                        float(work_experience_total_month_past5) / 12.00)

            if (row[39].find(name) != -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[42])
                m_year = regex_year.findall(row[42])
                m_month = regex_month.findall(row[42])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year_past6 = work_experience_total_year_past6 + str_year_num
                work_experience_total_month_past6 = work_experience_total_month_past6 + str_month_num
                work_year_past6 = float(work_experience_total_year_past6) + (
                        float(work_experience_total_month_past6) / 12.00)

            result = []
            result.append(row[0])
            result.append(work_year_past1)
            result.append(work_year_past2)
            result.append(work_year_past3)
            result.append(work_year_past4)
            result.append(work_year_past5)
            result.append(work_year_past6)

            writer.writerow(result)
            i = i + 1
    csvfile.close()


def generateweighting_expect_newest():
    fields1 = ['id', 'highest_degree']
    fields2 = ['work_year']
    fields3 = ['exp_time']
    fields4 = ['cosine_similarity_value']
    colnames1 = ['id', 'highest_degree']
    colnames2 = ['id', 'work_year_past1', 'work_year_past2', 'work_year_past3', 'work_year_past4', 'work_year_past5',
                 'work_year_past6']
    colnames3 = ['id', 'exp_time']
    colnames4 = ['id', 'cosine_similarity_value']
    id = []
    highest_degree = []
    work_year_past1 = []
    work_year_past2 = []
    work_year_past3 = []
    work_year_past4 = []
    work_year_past5 = []
    work_year_past6 = []
    exp_time = []
    cosine_similarity = []
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    id = id + (df['id'].tolist())
    highest_degree = highest_degree + df['highest_degree'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
        names=colnames1, skipinitialspace=True, usecols=fields1)
    id = id + (df['id'].tolist())
    highest_degree = highest_degree + df['highest_degree'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past1 = work_year_past1 + df['work_year_past1'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past2 = work_year_past2 + df['work_year_past2'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past3 = work_year_past3 + df['work_year_past3'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past4 = work_year_past4 + df['work_year_past4'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past5 = work_year_past5 + df['work_year_past5'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past6 = work_year_past6 + df['work_year_past6'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past1 = work_year_past1 + df['work_year_past1'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past2 = work_year_past2 + df['work_year_past2'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past3 = work_year_past3 + df['work_year_past3'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past4 = work_year_past4 + df['work_year_past4'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past5 = work_year_past5 + df['work_year_past5'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
        names=colnames2, skipinitialspace=True, usecols=fields2)
    work_year_past6 = work_year_past6 + df['work_year_past6'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
        names=colnames3, skipinitialspace=True, usecols=fields3)
    exp_time = exp_time + df['exp_time'].tolist()
    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
        names=colnames3, skipinitialspace=True, usecols=fields3)
    exp_time = exp_time + df['exp_time'].tolist()

    df = pd.read_csv(
        globalparameter.path + globalparameter.output_file_header_job_title + 'cosine_similarity_test.csv',
        names=colnames4, skipinitialspace=True, skiprows=2, usecols=fields4)
    cosine_similarity = cosine_similarity + df['cosine_similarity_value'].tolist()

    length_id = len(id)
    length_highest_degree = len(highest_degree)
    length_exp_time = len(exp_time)
    length_cosine_similarity = len(cosine_similarity)

    frame = pd.DataFrame({'id': id, 'highest_degree': highest_degree, 'work_year_past1': work_year_past1,
                          'work_year_past2': work_year_past2, 'work_year_past3': work_year_past3,
                          'work_year_past4': work_year_past4, 'work_year_past5': work_year_past5,
                          'work_year_past6': work_year_past6, 'exp_time': exp_time,
                          'cosine_similarity': cosine_similarity})

    frame.to_csv(globalparameter.path + '/test.csv')
