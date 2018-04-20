import csv
import re

def calculatehighestdegree():
    degree_index = 8
    for i in range(len(regex_list)):
        regex_highestdegree = re.compile(regex_list[i])
        # print(row[46])
        m_highest_degree = regex_highestdegree.findall(row[46])
        print(m_highest_degree)
        if not m_highest_degree and degree_index>=8:
            degree_index = 8
        else:
            if degree_index>i:
                degree_index = i
            # if i == 0:
            #     degree_index = 3
            # elif i >= 1 and i <= 3:
            #     degree_index = 2
            # elif i >= 1 and i <= 3:
            #     degree_index = 1
        # print(degree_index)
    return degree_index

# , open('output.csv','w') as outputfile
with open('/Users/pengyuzhou/Desktop/software_engineer_lowercase_no_punctuation.csv', 'r') as csvfile:
    name = 'software engineer'
    reader = csv.reader(csvfile)
    # writer = csv.DictWriter(outputfile)
    counter = 1
    regex_list = ['(ph ?d ?)', '(ms)', '(master)','(mba)', '(b ?s)', '(b ?e)' , '(bachelor)']
    writer = csv.writer(open('/Users/pengyuzhou/Desktop/marketing_manager_lowercase_no_punctuation.csv', 'w'))
    writer1 = csv.writer(open('/Users/pengyuzhou/Desktop/non_marketing_manager_lowercase_no_punctuation.csv', 'w'))
    for row in reader:
        # print(i)
        highest_degree = 0
        if (row[3].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[9].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[15].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[21].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[27].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[33].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        elif (row[39].find(name) != -1):
            degree_num = calculatehighestdegree()
            if highest_degree < degree_num:
                highest_degree = degree_num
        print('user num = {}. highest degree = {}'.format(counter, highest_degree))
        counter = counter + 1

csvfile.close()
# outputfile.close()

