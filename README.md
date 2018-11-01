# Content-Based-Talent-Recommendation-of-LinkedIn-Profile

# Aim
This project is for content-based recommedation for talents, we used different combinations of different technologies such as feature representation approachs(N-Grams, Word Embedding) and different learning algorithms(SVM, Logistic regression) to find the best approach for expert recommendaion of LinkedIn user profiles.

# Data Analysis of LinkedIn Profile

Data overview:
![Snippet of cleaned data set](https://github.com/YuzhouPeng/images/blob/master/cleaneduserdata.png)

The LinkedIn user profile data is a 261.2 MB CSV file with 158096 LinkedIn user profile. 

For every user profile, they have 67 attributes that can be categorized as following:
1. User id
2. Username
3. Connections number of user
4. Seven parts of work experience (current and past work experience, combined
with job title, company name, company type, work duration, company location)
5. Four parts of educational backgrounds (university name, degree of education,
major, end date of education, education details) 6. Skills
7. Languages

Top 15 job position:
![Top 15 job position](https://github.com/YuzhouPeng/images/blob/master/top15%20job%20position.png)

Number of the effective work experience:
![Effective work experience value](https://github.com/YuzhouPeng/images/blob/master/number%20of%20effective%20value%20in%20work%20experience.png)

Number of effective education:
![Effective education value](https://github.com/YuzhouPeng/images/blob/master/num%20of%20value%20in%20edu.png)


and the organization of the user profile is:
![organization of the user profile is](https://github.com/YuzhouPeng/images/blob/master/organization%20of%20user%20profile%20class.png)

In order to make the robustness and scalability of the system, we use the Objected-Oriented (OO based) programming in our system, and the organization is shown in the linkedindata_old.py.

# Feature representation lists:

N-gram models used:

Unigram(Bag-of-Words)

![unigram model](https://github.com/YuzhouPeng/images/blob/master/unigram.png)

Bigram

![Bigram model](https://github.com/YuzhouPeng/images/blob/master/bigram.png)

Trigram

![Trigram model](https://github.com/YuzhouPeng/images/blob/master/trigram.png)

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
