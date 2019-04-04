import csv,globalparameter,re,itertools,jobtitleextractor



def matrix_generator_train(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer,indexnumber):
    name = jobtitle_name
    content1 = []
    content2 = []
    job_title_list  = jobtitleextractor.extract_jobtitle(indexnumber)
    # , open('output.csv','w') as outputfile

        # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 0
    flag = 0
    index_list = [3,9,15,21,27,33,39]
    for row in itertools.islice(reader,0,500):
        for index in range(len(index_list)):
            test1 = row[index_list[index]]
            try:
                find_index = job_title_list.index(row[index_list[index]])
                content1.append(row[0])
                content1.append(index_list[index])
                content1.append(find_index+1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
            except:
                content1.append(row[0])
                content1.append(index_list[index])
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
                j = j + 1
        writer.writerows(content2)
        content2 = []
        # i = i + 1
        j = 0

    # writer = csv.DictWriter(outputfile)
    j = 0
    i = 0
    list1 = [9, 15, 21, 27, 33, 39]

    for row in itertools.islice(reader1,0,500):
        for index in range(len(index_list)):
            test1 = row[index_list[index]]
            try:
                find_index = job_title_list.index(row[index_list[index]])
                content1.append(row[0])
                content1.append(index_list[index])
                content1.append(find_index)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
            except:
                content1.append(row[0])
                content1.append(index_list[index])
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
                j = j + 1
        writer.writerows(content2)
        content2 = []
        # i = i + 1
    sparsityrate = float(have1) / (float(donthave)+float(have1))
    print(jobtitle_name+" sparsity of train: %.4f" % sparsityrate)

    # outputfile.close()