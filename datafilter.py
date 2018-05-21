import csv


# , open('output.csv','w') as outputfile
def filter_alluser_with_jobtitle(filepath,outputfilepath,name_for_search):


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
def filter_alluser_with_newest_jobtitle(filepath,outputfilepath,name_for_search):


    with open('/Users/pengyuzhou/Desktop/LinkedIn_data_lowercase_no_punctuation.csv', 'r') as csvfile:
        name = 'marketing manager'
        reader = csv.reader(csvfile)
        # writer = csv.DictWriter(outputfile)
        i = 1
        writer = csv.writer(open('/Users/pengyuzhou/Desktop/marketing_manager_lowercase_no_punctuation.csv', 'w'))
        for row in reader:
            print(i)
            if (row[3].find(name) != -1):
                writer.writerow(row)
            i = i + 1

    csvfile.close()