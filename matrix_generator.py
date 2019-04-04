import csv,globalparameter,re,itertools,jobtitleextractor



def matrix_generator_train(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer,indexnumber):
    name = jobtitle_name
    content1 = []
    content2 = []
    job_title_list  = jobtitleextractor.extract_jobtitle(indexnumber)
    # , open('output.csv','w') as outputfile
    regex_year = re.compile('((\d+)\s+years?)')

        # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 0
    for row in itertools.islice(reader,0,500):
        item_rating_list = [0]*len(job_title_list)
        for k in range(len(job_title_list)):
            if job_title_list[k] == row[3]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[9]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[15]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[21]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[27]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[33]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[39]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
        for index in range(len(item_rating_list)):
            if item_rating_list[index]:
                have1 = have1+1
            else:
                donthave = donthave+1
        for index in range(len(item_rating_list)):
            content1.append(row[0])
            content1.append(index)
            content1.append(item_rating_list[index])
            content2.append(content1)
            content1 = []
        writer.writerows(content2)
        content2 = []
        # i = i + 1
        j = 0

    # writer = csv.DictWriter(outputfile)
    j = 0
    i = 0
    list1 = [9, 15, 21, 27, 33, 39]

    for row in itertools.islice(reader1,0,500):
        item_rating_list = [0]*len(job_title_list)
        for k in range(len(job_title_list)):
            if job_title_list[k] == row[3]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[9]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[15]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[21]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[27]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[33]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
            if job_title_list[k] == row[39]:
                item_rating_list[k] = item_rating_list[k]+1
            j = j + 1
        for index in range(len(item_rating_list)):
            if item_rating_list[index]:
                have1 = have1+1
            else:
                donthave = donthave+1
        for index in range(len(item_rating_list)):
            content1.append(row[0])
            content1.append(index)
            content1.append(item_rating_list[index])
            content2.append(content1)
            content1 = []
        writer.writerows(content2)
        content2 = []
        # i = i + 1
    sparsityrate = float(have1) / (float(donthave)+float(have1))
    print(jobtitle_name+" sparsity of train: %.4f" % sparsityrate)

    # outputfile.close()