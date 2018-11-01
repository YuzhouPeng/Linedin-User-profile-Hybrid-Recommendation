# Content-Based-Talent-Recommendation-of-LinkedIn-Profile

# Aim
This project is for content-based recommedation for talents, we used different combinations of different technologies such as feature representation approachs(N-Grams, Word Embedding) and different learning algorithms(SVM, Logistic regression) to find the best approach for expert recommendaion of LinkedIn user profiles.

# Data Analysis of LinkedIn Profile

# Feature representation lists:

N-gram models used:

Unigram(Bag-of-Words)

Bigram

Trigram

Machine learning algorithms used:

Logistic Regression

Logistic Regression CV

SVM SVC

SVM NuSVC

SVM LinearSVC

Naive Bayes

Decision Tree

Random Forest


Data Description:
The LinkedIn profile is combined with following content:

1.user id

2.user name 

3.connections number of user 

4.six parts of work experience(combined with job title, company name, company type, work duration, company location) 

5.Highest education background 

6.Three parts of other education background

7.skills and languages



The function of python file:

datafilter.py: filter the data into two different dataset based on the aim of the recommendation (users who are relevanat and users who are not relevant)

calculate_data_job_now.py: calculate user's work year of past work experience using regular experssion

datanormalize.py: normalize results of the work year data

bag-of-words.py: generate data based on bag-of-words

n-grams.py: generate data based-on bigram or trigram

generate_train_test_set.py: generate train and test set

generateweightingfile.py: merge user data with normalized work year data.

globalparameter.py: store the global parameter of the data, including the data path,train/test split ratio and other parameter.

main.py: main function of the program.
