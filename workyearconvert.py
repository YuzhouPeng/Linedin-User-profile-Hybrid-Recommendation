import csv
import re
# , open('output.csv','w') as outputfile
with open('/Users/pengyuzhou/Desktop/software_engineer_lowercase_no_punctuation.csv', 'r') as csvfile:
    name = 'software engineer'
    reader = csv.reader(csvfile)
    # writer = csv.DictWriter(outputfile)
    i = 1
    writer = csv.writer(open('/Users/pengyuzhou/Desktop/marketing_manager_lowercase_no_punctuation.csv', 'w'))
    writer1 = csv.writer(open('/Users/pengyuzhou/Desktop/non_marketing_manager_lowercase_no_punctuation.csv', 'w'))
    for row in reader:
        # print(i)
        work_experience_total_year = 0
        work_experience_total_month = 0
        if (row[3].find(name)!=-1):
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
            work_experience_total_year = work_experience_total_year +str_year_num
            work_experience_total_month = work_experience_total_month +str_month_num
            # print('year num = {} month num = {}'.format(str_year_num, str_month_num))

        if (row[9].find(name)!=-1):
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
        if (row[15].find(name)!=-1):
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
        if (row[21].find(name)!=-1):
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
        if (row[27].find(name)!=-1):
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
        if (row[33].find(name)!=-1):
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
        if (row[39].find(name)!=-1):
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
        work_year = float(work_experience_total_year)+(float(work_experience_total_month)/12.00)

        print('user num = {}. work year: {:10.4f}'.format(i,work_year))
        i = i + 1

csvfile.close()
# outputfile.close()
