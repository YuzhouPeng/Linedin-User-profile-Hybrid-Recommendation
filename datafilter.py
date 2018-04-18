import csv

# , open('output.csv','w') as outputfile
with open('/Users/pengyuzhou/Desktop/LinkedIn_data_lowercase_no_punctuation.csv', 'r') as csvfile:
    name = 'mechanical engineer'
    reader = csv.reader(csvfile)
    # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 1
    writer = csv.writer(open('/Users/pengyuzhou/Desktop/mechanical_engineer_data_lowercase_no_punctuation.csv', 'w'))
    for row in reader:
        print(i)
        if (row[3].find(name)!=-1):
            writer.writerow(row)
        elif (row[9].find(name)!=-1):
            writer.writerow(row)
        elif (row[15].find(name)!=-1):
            writer.writerow(row)
        elif (row[21].find(name)!=-1):
            writer.writerow(row)
        elif (row[27].find(name)!=-1):
            writer.writerow(row)
        elif (row[33].find(name)!=-1):
            writer.writerow(row)
        elif (row[39].find(name)!=-1):
            writer.writerow(row)
        i = i + 1

csvfile.close()
# outputfile.close()
