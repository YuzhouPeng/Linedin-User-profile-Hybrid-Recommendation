import workexperiecetimes, non_calculatedegreeworkyear, calculatedegreeworkyear, datanormalize, generateweightingfile, \
    calculatecosinesimilarity
import globalparameter
import time

if __name__ == '__main__':
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.job_title_data_path,
                                                globalparameter.output_file_header_job_title,globalparameter.extract_number)
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.job_title_data_path,
                                                globalparameter.output_file_header_non_job_title,1000-globalparameter.extract_number)
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

    time.sleep(5)
    #
    # datanormalize.normalize_highest_degree(
    #     globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
    #     globalparameter.output_file_header_job_title, globalparameter.name_for_search_highest_degree)
    # time.sleep(1)
    # datanormalize.normalize_workyear_exptime(
    #     globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
    #     globalparameter.output_file_header_job_title, globalparameter.name_for_search_work_year)
    # time.sleep(1)
    #
    # datanormalize.normalize_highest_degree(
    #     globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_highest_degree + globalparameter.output_file_root,
    #     globalparameter.output_file_header_non_job_title, globalparameter.name_for_search_highest_degree)
    # time.sleep(1)
    #
    # datanormalize.normalize_workyear_exptime(
    #     globalparameter.path + globalparameter.output_file_header_non_job_title + globalparameter.name_for_search_work_year + globalparameter.output_file_root,
    #     globalparameter.output_file_header_non_job_title, globalparameter.name_for_search_work_year)
    # time.sleep(1)
    #
    # datanormalize.normalize_workyear_exptime(
    #     globalparameter.path + globalparameter.output_file_header_job_title + globalparameter.name_for_search_exp_times + globalparameter.output_file_root,
    #     globalparameter.output_file_header_job_title, globalparameter.name_for_search_exp_times)
    # time.sleep(1)
    calculatecosinesimilarity.content_based_doc_generator(globalparameter.extract_number)
    calculatecosinesimilarity.calculatecosinesililarity()
    generateweightingfile.generateweighting()
    datanormalize.normalize_weighting_highest_degree(globalparameter.path + '/test.csv')


    print(1)
