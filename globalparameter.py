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
total_number = 10

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
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/secretary',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/project_manager',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/mechanical_engineer',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/marketing_manager',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/financial_advisor',
              '/Users/pengyuzhou/Google Drive/Linkedin_datafile/data_scientist']
