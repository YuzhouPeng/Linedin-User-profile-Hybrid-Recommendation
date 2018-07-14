from nltk import ngrams
from nltk.corpus import stopwords
import collections, globalparameter, time
import pandas as pd
from sklearn.decomposition import TruncatedSVD

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


# datapath = globalparameter.folderpath[0]+'/'+'output_pos_for_dummy.csv'
# non_datapath = globalparameter.folderpath[0]+'/'+'output_neg_for_dummy.csv'
# column_index_list = globalparameter.extract_column_list
def extractall_information_n_gram(datapath, non_datapath, column_index_list, gram_number):
    # extract columns:[3-5,9-11,15-17,21-23,27-29,33-35,39-41]
    #education:[45-65 length5][46-47,49,51-52,54,56-57,59,61-62,64]
    #skill language:[65,66]
    #-1
    # can not extract column: [7,13,19,25,31,37,43]
    # work year column: []
    # year column: [49,54,59,64]
    # school column: [46,51,56,61]
    # total column number: 67
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    all_info_list = []
    user_data = user_data.fillna("")
    non_user_data = non_user_data.fillna("")
    for i in range(len(column_index_list)):
        column_index = column_index_list[i]
        df = pd.concat([user_data.iloc[:, [column_index]],
                        non_user_data.iloc[:, [column_index]]]).values.tolist()
        all_info_list.append(df)

    user_data = []
    for j in range(1000):
        user_row = []
        for i in range(len(all_info_list)):
            user_row.append(all_info_list[i][j])
        user_data.append(user_row)
    user_total_info_data = []
    user_total_words_info_data1 = []
    user_company_data_for_dummy = pd.DataFrame()

    for i in range(len(user_data)):
        user_data[i] = flatten(user_data[i])
    # print(df)
    for i in range(len(user_data)):
        user_total_info_data.append(' '.join(str(k) for k in user_data[i]))
    # print(user_skill_data)

    # #remove all numerical number
    for i in range(len(user_total_info_data)):
        user_total_info_data[i] = ''.join([x for x in user_total_info_data[i] if not x.isdigit()])

    for i in range(len(user_total_info_data)):
        user_total_words_info_data1.append(user_total_info_data[i].split())
    # print(user_skill_data1)

    bigram_list = []
    stopset = set(stopwords.words('english'))
    # generate n-grams without stopwords
    for i in range(len(user_total_words_info_data1)):
        n_grams = ngrams(user_total_words_info_data1[i],gram_number)
        new_n_gram = []
        for gram in n_grams:
            remove_stopword_gram = [x for x in list(gram) if x not in stopset]
            new_n_gram.append(' '.join(remove_stopword_gram))
        bigram_list.append(new_n_gram)


    user_total_words_info_data1 = pd.DataFrame({'all_data': user_total_words_info_data1})
    # print(user_skill_data1)
    length1 = len(user_total_words_info_data1)

    i = 0
    new_user_total_words_info_data1 = []
    # for i in range(len(user_total_words_info_data1)):
    #     new_user_total_words_info_data1.append([x for x in user_total_words_info_data1[i] if x != 'nan'])

    # print(user_company_data_for_dummy)
    total_words_variable_array = pd.get_dummies(pd.DataFrame(bigram_list), drop_first=True)

    # reduce dimention using svd
    svd = TruncatedSVD(50)
    total_words_transformed = svd.fit_transform(total_words_variable_array)

    column_names = ['column_' + str(i) for i in range(50)]
    total_words_transformed = pd.DataFrame(total_words_transformed,columns=column_names)
    shape_of_words = total_words_variable_array.shape
    # print(total_words_variable_array.shape)
    print(total_words_transformed.shape)
    return total_words_transformed

