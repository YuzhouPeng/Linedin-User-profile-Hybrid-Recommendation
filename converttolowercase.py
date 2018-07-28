import fileinput

for line in fileinput.input("/Users/pengyuzhou/Google Drive/Linkedin_datafile/data_v3.csv", inplace=1):
    print(line.lower(), end='')