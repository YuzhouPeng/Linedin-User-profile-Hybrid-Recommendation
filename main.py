import workexperiecetimes, non_calculatedegreeworkyear, calculatedegreeworkyear, datanormalize, generateweightingfile, \
    calculatecosinesimilarity, diagramgenerator
import globalparameter
import time


def contentbased(positivesamplevalue):
    globalparameter.extract_number = positivesamplevalue
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.job_title_data_path,
                                                globalparameter.output_file_header_job_title,
                                                globalparameter.extract_number)
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.job_title_data_path,
                                                globalparameter.output_file_header_non_job_title,
                                                (1000 - globalparameter.extract_number))
    calculatedegreeworkyear.calculate_highest_degree(globalparameter.path, globalparameter.job_title_name,
                                                     globalparameter.job_title_data_path,
                                                     (globalparameter.extract_number))
    calculatedegreeworkyear.calculate_work_year(globalparameter.path, globalparameter.job_title_name,
                                                globalparameter.job_title_data_path,
                                                globalparameter.extract_number)
    non_calculatedegreeworkyear.non_calculate_highest_degree(globalparameter.path, globalparameter.job_title_name,
                                                             globalparameter.non_job_title_data_path,
                                                             (globalparameter.extract_number))
    non_calculatedegreeworkyear.non_calculate_work_year(globalparameter.path, globalparameter.job_title_name,
                                                        globalparameter.non_job_title_data_path,
                                                        (globalparameter.extract_number))

    time.sleep(1)
    calculatecosinesimilarity.content_based_doc_generator(globalparameter.extract_number)
    calculatecosinesimilarity.calculatecosinesililarity()
    generateweightingfile.generateweighting()
    datanormalize.normalize_weighting_highest_degree(globalparameter.path + '/test.csv')
    diagramgenerator.calculateprecisionandrecall(globalparameter.extract_number)

def function(index):
    contentbased(index)
    diagramgenerator.generatediagram(globalparameter.cosine_similarity_column_precision,
                                     globalparameter.cosine_similarity_column_recall,
                                     globalparameter.name_for_search_cosine_similarity, index,1)
    diagramgenerator.generatediagram(globalparameter.work_year_column_precision,
                                     globalparameter.work_year_column_recall,
                                     globalparameter.name_for_search_work_year, index,2)
    diagramgenerator.generatediagram(globalparameter.highest_degree_column_precision,
                                     globalparameter.highest_degree_column_recall,
                                     globalparameter.name_for_search_highest_degree, index,3)
    diagramgenerator.generatediagram(globalparameter.exp_time_column_precision,
                                     globalparameter.exp_time_column_recall,
                                     globalparameter.name_for_search_exp_times, index,4)
    globalparameter.cosine_similarity_column_precision = []
    globalparameter.cosine_similarity_column_recall = []
    globalparameter.work_year_column_precision = []
    globalparameter.work_year_column_recall = []
    globalparameter.highest_degree_column_precision = []
    globalparameter.highest_degree_column_recall = []
    globalparameter.exp_time_column_precision = []
    globalparameter.exp_time_column_recall = []

if __name__ == '__main__':
    for i in range(100,900,100):
        function(i)
    print(1)
