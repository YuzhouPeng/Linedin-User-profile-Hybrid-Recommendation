# job_title_name is the name of relevant job like 'software engineer'
job_title_name = 'financial accountant'

# job_title_data_path is the path of relevant job data
job_title_data_path = '/Users/pengyuzhou/Google Drive/Linkedin_datafile/financial_accountant/financial_accountant_lowercase_no_punctuation.csv'

# non_job_title_data_path is the path of non-relevant job data
non_job_title_data_path = '/Users/pengyuzhou/Google Drive/Linkedin_datafile/financial_accountant/non_financial_accountant_lowercase_no_punctuation.csv'

# path is folder path of all data
path = '/Users/pengyuzhou/Google Drive/Linkedin_datafile/financial_accountant'

# name_for_features
name_for_search_exp_times = 'suitable_work_experience_times'
name_for_search_highest_degree = 'highest_degree'
name_for_search_work_year = 'work_year'
name_for_search_cosine_similarity = 'cosine_similarity'

# number for extraction of numbers
extract_number = 500
total_number = 1000
ratio = 0.5
# format for output file
output_file_header_job_title = '/financial_accountant_'
output_file_header_non_job_title = '/non_financial_accountant_'
output_file_root = '_lowercase_no_punctuation.csv'

# lists to store precision and recall value
cosine_similarity_column_precision = []
cosine_similarity_column_recall = []
work_year_column_precision = []
work_year_column_recall = []
highest_degree_column_precision = []
highest_degree_column_recall = []
exp_time_column_precision = []
exp_time_column_recall = []

folderpath = ['/Users/pengyuzhou/Google Drive/Linkedin_datafile/software_engineer',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/project_manager',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/research_assistant',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/process_engineer',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/consultant',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/account_manager']

jobtitle_list = ['software engineer', 'project manager', 'research assistant', 'process engineer', 'consultant',
                 'account manager']
jobtitle_path_list = ['software_engineer', 'project_manager', 'research_assistant', 'process_engineer', 'consultant',
                      'account_manager']

raw_data_path = '/Users/pengyuzhou/Google Drive/Linkedin_datafile/LinkedIn_data_lowercase_no_punctuation.csv'
# extract columns:[3-5,9-11,15-17,21-23,27-29,33-35,39-41]
# education:[45-65 length5][46-47,49,51-52,54,56-57,59,61-62,64]
# skill language:[65,66]
extract_column_list = [9,10,11,15,16,17,21,22,23,27,28,29,33,34,35,39,40,41,46,47,49,51,52,54,56,57,59,61,62,64,65,66]

extract_work_experience_list = [9,10,11,15,16,17,21,22,23,27,28,29,33,34,35,39,40,41]

extract_education_background_list = [46,47,49,51,52,54,56,57,59,61,62,64]

extract_skills_list = [65,66]

train_pos_start_loc = 0
train_neg_start_loc = extract_number
train_pos_end_loc = int(extract_number * ratio)
train_neg_end_loc = extract_number + int((total_number - extract_number) * ratio)
test_pos_start_loc = int(extract_number * ratio)
test_neg_start_loc = extract_number + int((total_number - extract_number) * ratio)
test_pos_end_loc = extract_number
test_neg_end_loc = total_number

alg_precision = [0]*48
alg_recall = [0]*48
alg_accuracy = [0]*48
alg_f1_score = [0]*48
time = [0]*48
