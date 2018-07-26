import globalparameter, csv, re, linkedindata
import random
import itertools
import pandas as pd
import numpy as np


def calculate_work_year_except_newest(folderpath, job_title_data_path, jobtitlename, name_for_search):
    with open(
            job_title_data_path,
            'r') as csvfile:
        name = name_for_search
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(
            open(
                folderpath + '/' + jobtitlename + '_' + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
                'w'))
        for row in reader:
            # print(i)
            # for row in reader:
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


def calculate_work_year_oo(classlist):
    total_work_duration_list = []
    work_duration_per_user_total_list = []
    for i in range(len(classlist)):
        total_work_duration_list.append(classlist[i].past_work_duration_value())
    for i in range(10):
        work_duration_per_user_list = []
        past_work_year = [k[i] for k in total_work_duration_list]
        regex_year = re.compile('((\d+)\s+years?)')
        regex_month = re.compile('((\d+)\smonths?)')
        for i in range(len(past_work_year)):
            m_year = regex_year.findall(past_work_year[i])
            m_month = regex_month.findall(past_work_year[i])
            if not m_year:
                str_year_num = 0
            else:
                str_year_num = int(m_year[0][1])
            if not m_month:
                str_month_num = 0
            else:
                str_month_num = int(m_month[0][1])
            work_duration_per_user_total = float(str_year_num) + (
                    float(str_month_num) / 12.00)
            work_duration_per_user_list.append(work_duration_per_user_total)
        work_duration_per_user_total_list.append(work_duration_per_user_list)
        print(1)
    return work_duration_per_user_total_list
