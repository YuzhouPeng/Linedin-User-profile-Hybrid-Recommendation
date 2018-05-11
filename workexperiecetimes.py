import csv
import itertools
import globalparameter

# , open('output.csv','w') as outputfile
def calculate_work_exp_times(path, name_for_search, job_title_name, input_file_path,output_file_header):
    with open(
            input_file_path,
            'r') as csvfile:
        name = job_title_name
        reader = csv.reader(csvfile)
        counter = 1
        writer = csv.writer(open(path + output_file_header + name_for_search + globalparameter.output_file_root, 'w'))
        for row in itertools.islice(reader, 501):
            # print(i)
            suitable_work_experience_times = 0
            if (row[3].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[9].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[15].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[21].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[27].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[33].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            if (row[39].find(name) != -1):
                suitable_work_experience_times = suitable_work_experience_times + 1
            print('user num = {}. suitable work experience time = {}'.format(counter, suitable_work_experience_times))
            result = []
            result.append(row[0])
            result.append(suitable_work_experience_times)
            writer.writerow(result)
            counter = counter + 1
    csvfile.close()
