from sklearn import preprocessing
import pandas as pd

fields = ['id','degree']
df = pd.read_csv('/Users/pengyuzhou/Desktop/non_software_engineer_highest_degree_lowercase_no_punctuation.csv', skipinitialspace=True, usecols=fields)


x = df.values #returns a numpy array
degree = []
#iteration of the highest degree
for row in df['degree']:
    if row == 1:
        degree.append(3)
    elif row >=2 and row<=4:
        degree.append(2)
    elif row >=5 and row<=7:
        degree.append(1)
    else:
        degree.append(0)
    
degree = pd.DataFrame(degree, columns=['degree'])
df['degree'] = degree['degree']
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled= min_max_scaler.fit_transform(df)
#x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
normalzied_value = pd.DataFrame(x_scaled,columns=['normalized_id','normalized_degree']).to_csv('/Users/pengyuzhou/Desktop/non_software_engineer_highest_degree_normalize.csv')


from sklearn import preprocessing
import pandas as pd

fields = ['id','year']
df = pd.read_csv('/Users/pengyuzhou/Desktop/non_software_engineer_work_year_lowercase_no_punctuation.csv', skipinitialspace=True, usecols=fields)


x = df.values #returns a numpy array
#iteration of the highest degree

    
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled= min_max_scaler.fit_transform(x)
#x_scaled.to_csv('/Users/pengyuzhou/Desktop/software_engineer_work_year_normalize.csv')
normalzied_value = pd.DataFrame(x_scaled,columns=['normalized_id','normalized_year']).to_csv('/Users/pengyuzhou/Desktop/non_software_engineer_work_year_normalize.csv')