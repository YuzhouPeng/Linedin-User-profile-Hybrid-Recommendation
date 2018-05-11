import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.feature_selection import RFECV

length = 500
df = pd.read_csv('/Users/pengyuzhou/Desktop/content_based_software_engineer/content_based_software_engineer_weighting.csv',sep = ',')
id_column = df['id']
cosine_similarity_column = df['cosine_similarity_value']
work_year_column = df['work_year_value']
highest_degree_column = df['highest_degree_value']
user_data = pd.DataFrame({'id':id_column, 'cosine_similarity':cosine_similarity_column, 'work_year':work_year_column, 'highest_degree':highest_degree_column})

sorted_id_cosine_similarity = user_data.sort_values('cosine_similarity', ascending = False).groupby('id').head(500)
sorted_id_work_year = user_data.sort_values('work_year', ascending = False).groupby('id').head(500)
sorted_id_highest_degree = user_data.sort_values('highest_degree', ascending = False).groupby('id').head(500)
sorted_id_cosine_similarity_top500 = sorted_id_cosine_similarity['id'][:length].tolist()

cosine_similarity_top500 = user_data['id'].values[:length].tolist()
cosine_similarity_other = user_data['id'].values[length:1000].tolist()
work_year_top500 = sorted_id_work_year['id'][:length].tolist()
id_manual_top500 = id_column[:length]

id_positive = cosine_similarity_top500
id_negative = cosine_similarity_other
sorted_id_work_year_top500= sorted_id_work_year['id'][:length].tolist()
sorted_id_work_year_other = sorted_id_work_year['id'][1000-length:1000].tolist()
id_true_positive = []
id_true_negative = []
id_false_positive = []
id_false_negative = []

for i in range(length):
    if sorted_id_work_year_other[i] in id_negative:
        id_true_negative.append(cosine_similarity_top500[i])
for i in range(length):
    if sorted_id_work_year_top500[i] in id_positive:
        id_true_positive.append(cosine_similarity_top500[i])
for i in range(length):  
    if sorted_id_work_year_top500[i] in id_negative:
        id_false_negative.append(cosine_similarity_top500[i])
for i in range(length):
    if sorted_id_work_year_other[i] in id_positive:
        id_false_positive.append(cosine_similarity_other[i])

num_true_positive = len(id_true_positive)
num_true_negative = len(id_true_negative)
num_false_positive = len(id_false_positive)
num_false_negative = len(id_false_negative)

print(len(id_false_positive))
print(len(id_false_negative))
print(id_false_positive)
print(id_false_negative)
print('accuracy = {}'.format((num_true_positive+num_true_negative)/1000))
print('recall = {}'.format((num_true_positive)/(num_true_positive+num_false_negative)))
print('precision = {}'.format((num_true_positive)/(num_true_positive+num_false_positive)))

sorted_id_highest_degree_top500= sorted_id_highest_degree['id'][:length].tolist()
sorted_id_highest_degree_other = sorted_id_highest_degree['id'][1000-length:1000].tolist()
id_true_positive = []
id_true_negative = []
id_false_positive = []
id_false_negative = []

for i in range(length):
    if sorted_id_highest_degree_other[i] in id_negative:
        id_true_negative.append(cosine_similarity_top500[i])
for i in range(length):
    if sorted_id_highest_degree_top500[i] in id_positive:
        id_true_positive.append(cosine_similarity_top500[i])
for i in range(length):  
    if sorted_id_highest_degree_top500[i] in id_negative:
        id_false_negative.append(cosine_similarity_top500[i])
for i in range(length):
    if sorted_id_highest_degree_other[i] in id_positive:
        id_false_positive.append(cosine_similarity_other[i])

num_true_positive = len(id_true_positive)
num_true_negative = len(id_true_negative)
num_false_positive = len(id_false_positive)
num_false_negative = len(id_false_negative)

print(len(id_false_positive))
print(len(id_false_negative))
print(id_false_positive)
print(id_false_negative)
print('accuracy = {}'.format((num_true_positive+num_true_negative)/1000))
print('recall = {}'.format((num_true_positive)/(num_true_positive+num_false_negative)))
print('precision = {}'.format((num_true_positive)/(num_true_positive+num_false_positive)))
