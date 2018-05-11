import csv
import re
import itertools
import globalparameter

def calculatehighestdegree(regex_list,row):
    degree_index = 8
    for i in range(len(regex_list)):
        regex_highestdegree = re.compile(regex_list[i])
        # print(row[46])
        m_highest_degree = regex_highestdegree.findall(row[46])
        print(m_highest_degree)
        if not m_highest_degree and degree_index >= 8:
            degree_index = 8
        else:
            if degree_index > i + 1:
                degree_index = i + 1
    return degree_index

# , open('output.csv','w') as outputfile
def non_calculate_highest_degree(path, job_title_name, non_job_title_data_path, extract_number):
    with open(
            non_job_title_data_path,
            'r') as csvfile:
        name = job_title_name
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        counter = 1
        regex_list = ['(ph ?d ?)', '(ms)', '(master)', '(mba)', '(b ?s)', '(b ?e)', '(bachelor)']
        writer = csv.writer(
            open(path + globalparameter.output_file_header_non_job_title+ globalparameter.name_for_search_highest_degree + globalparameter.output_file_root, 'w'))
        for row in itertools.islice(reader, extract_number):
            # print(i)
            highest_degree = 0
            if (row[3].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[9].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[15].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[21].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[27].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[33].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            elif (row[39].find(name) == -1):
                degree_num = calculatehighestdegree(regex_list,row)
                if highest_degree < degree_num:
                    highest_degree = degree_num
            print('user num = {}. highest degree = {}'.format(counter, highest_degree))
            result = []
            result.append(row[0])
            result.append(highest_degree)
            writer.writerow(result)
            counter = counter + 1


    csvfile.close()


# outputfile.close()

# , open('output.csv','w') as outputfile
def non_calculate_work_year(path, job_title_name, job_title_data_path, extract_number):


    with open(
            job_title_data_path,
            'r') as csvfile:
        name = job_title_name
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(
            open(path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root, 'w'))
        for row in itertools.islice(reader, extract_number):
            # print(i)
            work_experience_total_year = 0
            work_experience_total_month = 0
            if (row[3].find(name) == -1):
                regex_year = re.compile('((\d+)\s+years?)')
                regex_month = re.compile('((\d+)\smonths?)')
                print(row[6])
                m_year = regex_year.findall(row[6])
                m_month = regex_month.findall(row[6])
                if not m_year:
                    str_year_num = 0
                else:
                    str_year_num = int(m_year[0][1])
                if not m_month:
                    str_month_num = 0
                else:
                    str_month_num = int(m_month[0][1])
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
                # print('year num = {} month num = {}'.format(str_year_num, str_month_num))

            if (row[9].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            if (row[15].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            if (row[21].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            if (row[27].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            if (row[33].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            if (row[39].find(name) == -1):
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
                work_experience_total_year = work_experience_total_year + str_year_num
                work_experience_total_month = work_experience_total_month + str_month_num
            work_year = float(work_experience_total_year) + (float(work_experience_total_month) / 12.00)

            print('user num = {}. work year: {:10.4f}'.format(i, work_year))
            result = []
            result.append(row[0])
            result.append(work_year)
            writer.writerow(result)
            i = i + 1

    csvfile.close()
# outputfile.close()
