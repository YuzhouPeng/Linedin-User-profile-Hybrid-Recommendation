import csv, globalparameter


# , open('output.csv','w') as outputfile
def filter_alluser_with_jobtitle(filepath, outputfilepath, name_for_search):
    with open('/Users/pengyuzhou/Desktop/LinkedIn_data_lowercase_no_punctuation.csv', 'r') as csvfile:
        name = 'marketing manager'
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(open('/Users/pengyuzhou/Desktop/marketing_manager_lowercase_no_punctuation.csv', 'w'))
        writer1 = csv.writer(open('/Users/pengyuzhou/Desktop/non_marketing_manager_lowercase_no_punctuation.csv', 'w'))
        for row in reader:
            print(i)
            if (row[3].find(name) != -1):
                writer.writerow(row)
            elif (row[9].find(name) != -1):
                writer.writerow(row)
            elif (row[15].find(name) != -1):
                writer.writerow(row)
            elif (row[21].find(name) != -1):
                writer.writerow(row)
            elif (row[27].find(name) != -1):
                writer.writerow(row)
            elif (row[33].find(name) != -1):
                writer.writerow(row)
            elif (row[39].find(name) != -1):
                writer.writerow(row)
            else:
                writer1.writerow(row)
            i = i + 1

    csvfile.close()


# outputfile.close()
def filter_alluser_with_newest_jobtitle(rawdatapath, folderpath,outputjobtitlepath, name_for_search):
    with open(rawdatapath, 'r') as csvfile:
        name = name_for_search
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(
            open(folderpath + '/' + outputjobtitlepath + globalparameter.output_file_root,
                 'w'))
        writer1 = csv.writer(
            open(folderpath + '/' +'non_'+ outputjobtitlepath + globalparameter.output_file_root,
                 'w'))
        for row in reader:
            print(i)
            if (row[3].find(name) != -1):
                writer.writerow(row)
            else:
                writer1.writerow(row)
            i = i + 1

    csvfile.close()

def filter_data_with_job_title_oo(classlist,jobtitle_name,index):
    result_list = []
    if index == 1:
        for i in range(len(classlist)):
            if classlist[i].title.find(jobtitle_name)!=-1:
                result_list.append(classlist[i])
    if index == 2:
        for i in range(len(classlist)):
            if classlist[i].title.find(jobtitle_name)==-1:
                result_list.append(classlist[i])
    return result_list