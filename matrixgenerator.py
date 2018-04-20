import csv
import fileinput
import re

lines = []
with open("/Users/pengyuzhou/Desktop/data.csv", "r") as input:
    lines = input.readlines()
