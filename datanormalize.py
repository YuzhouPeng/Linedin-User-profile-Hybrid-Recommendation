import csv
import pandas as pd
def normalize(df):
    result = df.copy()
    for row in df.columns:
        max_value = df[1].max()
        min_value = df[1].min()
        result[row] = (df[row] - min_value) / (max_value - min_value)
    return result

with open('/Users/pengyuzhou/Desktop/software_engineer_work_year_lowercase_no_punctuation.csv', 'r') as f:
    reader = csv.reader(f)
    writer = csv.writer(open('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv', 'w'))

    work_year_list = [float(i[1]) for i in reader]
    # print(work_year_list)
    max_work_year = max(work_year_list)
    min_work_year = min(work_year_list)

    count = 0
    for row1 in reader:
        print(row1[0])
        print(row1[0])

    for row in reader:
        count = count+1
        resultlist = []
        result = (float(row[1]) - min_work_year) / (max_work_year-min_work_year)
        # row.append(result)
        print('id = {} result = {}'.format(count, result))
        resultlist.append(row[0])
        resultlist.append(row[1])
        resultlist.append(result)
        writer.writerow(resultlist)
f.close()





