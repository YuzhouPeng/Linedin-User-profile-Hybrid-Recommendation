# Hybrid-Talent-Recommendation-of-LinkedIn

# Aim
This project is for Hybrid recommedation for talents, we used different combinations of different technologies such as feature representation approachs(N-Grams, Word Embedding) and different learning algorithms(SVM, Logistic regression) to find the best approach for expert recommendaion of LinkedIn user profiles.

# Content-based Recommender System Design
![recommender system framework](https://github.com/YuzhouPeng/images/blob/master/content-based%20recommender%20system%20design.png)


# LinkedIn Profile Data Overview and Data Analysis

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
major, end date of education, education details) 
6. Skills
7. Languages

Data analysis:

Connections number of user: the number shows the connections of other LinkedIn users for every user.


Top 15 job position of all user profile:
![Top 15 job position](https://github.com/YuzhouPeng/images/blob/master/top15%20job%20position.png)

Based on the statistic data, there are mainly three kinds of job position: technical position (engineer), management position(manager) and academic position(professor).

Thus, based on the data, we will mainly select job positions from those areas.

Average number of the effective work experience per user:
![Effective work experience value](https://github.com/YuzhouPeng/images/blob/master/number%20of%20effective%20value%20in%20work%20experience.png)
Based on the statistic data, nearly 82% of the user have at least 1 past job experience. And more than 48% of users have 2 job experience. 

Average number of effective education per user:
![Effective education value](https://github.com/YuzhouPeng/images/blob/master/num%20of%20value%20in%20edu.png)
Based on the statistic data, nearly 89% of the user have at least 1 education background. more than %56 of users have more than 2 education background.

Average number of the skills per user is: 19.72

Summary of the user data and selecting of user profile attributes:

Thus, based on the statistic data of the job position, education background and skills. We decided to use six past work experience, four parts of education (except university name, end date of education), skills, language.

# Coding sytle
In order to make the robustness and scalability of the system, we use the Objected-Oriented (OO based) programming in our system, and the organization is shown in the linkedindata_old.py and the organization of the user profile is:
![organization of the user profile is](https://github.com/YuzhouPeng/images/blob/master/organization%20of%20user%20profile%20class.png)





# Feature representation lists:

N-gram models used:

Unigram(Bag-of-Words)

![unigram model](https://github.com/YuzhouPeng/images/blob/master/unigram.png)

Bigram

![Bigram model](https://github.com/YuzhouPeng/images/blob/master/bigram.png)

Trigram

![Trigram model](https://github.com/YuzhouPeng/images/blob/master/trigram.png)

Word2vec:
![Word2vec](https://github.com/YuzhouPeng/images/blob/master/word2vec.png)

Doc2vec:
![Doc2vec](https://github.com/YuzhouPeng/images/blob/master/doc2vec.png)

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




# Collaborative-Filtering-User-Profile-Recommendation

# Design and Methodology of the Collaborative Filtering Approach

![Collaborative Filtering System Design](https://github.com/YuzhouPeng/images/blob/master/Screen%20Shot%202019-02-28%20at%2012.54.20.png)
The design of collaborative filtering is shown in figure. We will introduce main components in the collaborative filtering approach:
Data preprocessing: In the data preprocessing part we will discuss what attributes will be suitable for collaborative filtering approaches.
Forming matrix for learning algorithm: Process of forming user rating matrix will be presented and we will illustrate how we form the rating value for collaborative learning algorithm.


# Data preprocessing for Collaborative Filtering Recom- mendation
For the collaborative filtering approach, we usually need to form a matrix based on our goal for the recommendation. For example, for a recommendation in e-commerce, we usually need to form user-item matrix to find similarity between customers. For a similar book recommendation, we usually need to build item-item matrix to show the inner connection between books.
Thus in our collaborative filtering approach, we decided to form the matrix of user- workexperience-rating matrix (i.e. user as row of matrix, work experience attribute except the first work experience as columns of matrix and value in cells is the rating of work experience, which will be discussed thoroughly in the feature representation section) for collaborative filtering learning algorithms. The reason why we implement the strategy is that the collaborative filtering approach could fit our research aim (i.e. suitable approach for candidate recommendation for jobs). Thus we consider using work experience in the collaborative filtering approach. In order to build data for supervised learning, the job title of first work experience will be the output of learning and user-workexperience-rating matrix will be the output.


# Building Matrix for Collaborative Filtering Approach
We will build a user-workexperience-rating matrix based on the user profile data. The work experience (Columns of matrix) is six work experiences of a user mentioned in section 3.3 and we calculate the rating based on the following rules: For a specific given
32
job title (i.e. software engineer), we will calculate the rating based on following rules: 1. If the job title in the work experience is same as the given job title and the work
year is more or equal than 3 years, the rating value is 2.
2. If the job title in the work experience is the given job title and the work year is
less than 3 years, the rating value is 1.
3. If the job title in the work experience is not the given job title, the rating value
is -1.

![Build matrix of collaborative filtering](https://github.com/YuzhouPeng/images/blob/master/Screen%20Shot%202019-02-28%20at%2013.00.30.png)





# High Dimension of User Profile Vector Space and Solution

Some feature representation methods(like N-grams) will produce huge user profile vector space, which will cause longer training time of recommendation system.

The Dimension value of user profile using Bigram is:
![Dimension of bigram](https://github.com/YuzhouPeng/images/blob/master/Dimension%20value%20of%20generated%20feature%20vectors%20by%20Bigram%20.png)

Thus, we decided to use Singular Value Decomposition (SVD) for reducing the dimension to 50:

![Dimension after using SVD](https://github.com/YuzhouPeng/images/blob/master/Dimension%20value%20of%20generated%20feature%20vectors%20by%20Bigram.png)

Comparision of training time:

![Comparision of training time](https://github.com/YuzhouPeng/images/blob/master/Training%20time%20of%20different%20learning%20algorithms%20with%20original%20data%20and%20reduced%20dimension%20data.png)




# Recommendation Results:

We use precision and recall to evaluate results. The following is the evaluate results:

Average precision & recall of using all user profile data and N-gram model(work experience, education background, skill&language)
![precision1](https://github.com/YuzhouPeng/images/blob/master/Average%20precision%20for%20all%20job%20positions%20of%20using%20all%20data.png)

Average precision of using all user profile data and word embedding model(work experience, education background, skill&language)
![precision2](https://github.com/YuzhouPeng/images/blob/master/Word%20embedding%20approaches%20with%20highest%20precision%20for%20every%20job%20position.png)

Average precision of using all user profile data and document embedding model(work experience, education background, skill&language)
![precision3](https://github.com/YuzhouPeng/images/blob/master/Document%20embedding%20approaches%20with%20highest%20precision%20for%20every%20job%20position.png)

Here are part of results for recommenadtion result. For Further detailed information, please send me the message.
