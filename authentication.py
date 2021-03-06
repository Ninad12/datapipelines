import re
import config


def filename_validation(filename):
    split_config_file_template = config.filename_template.split('_')
    split_filename = filename.split('_')

    entity_index = split_config_file_template.index('EntityName')
    report_index = split_config_file_template.index('ReportName')
    frequency_index = split_config_file_template.index('Frequency')
    
    if split_filename[entity_index] in config.valid_entities and split_filename[report_index] in config.valid_reports and split_filename[frequency_index] in config.Valid_Frequencies and len(split_filename) == len(split_config_file_template):
        return True
    return False

def is_authenticate(filename):
    '''
     This function takes name of file and authenticate for .csv and .json format and return file format.
    '''
    split_filename = filename.split('.')

    if split_filename[-1] in config.Valid_Extensions:
        if filename_validation(filename):
            return (True, split_filename[-1])

    return (False, 0)
