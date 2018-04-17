import csv
import fileinput
import re
# csvFile = open("/Users/pengyuzhou/Desktop/data.csv","r")
# reader = csv.reader(csvFile)

# for line in fileinput.input("/Users/pengyuzhou/Dropbox/data.csv", inplace=1):
#     print(line.lower(), end='')

# for line in fileinput.input("/Users/pengyuzhou/Desktop/data.csv", inplace=1):
#     clean = line.translate(None, "[,.;@#?!&$]\ *")
#     print(clean, end='')

lines = []
with open("/Users/pengyuzhou/Desktop/data.csv", "r") as input:
    lines = input.readlines()

conversion = '=~`[.;@?!&$]\/*_-?'
newtext = ' '
outputLines = []
for line in lines:
    temp = line[:]
    for c in conversion:
        temp = temp.replace(c, newtext)
    outputLines.append(temp)

with open("/Users/pengyuzhou/Desktop/output_data.csv", 'w') as output:
    for line in outputLines:
        output.write(line + "\n")