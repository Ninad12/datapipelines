import csv
from io import StringIO
import fileReconConfig as config

def recon(filename):

    file_data = open(filename, "rb")
    read_data = file_data.read()

    original_data = StringIO(str(read_data,'utf-8'))
    reader = []

    split_filename = filename.split('.')
    get_split_filename = filename.split('_')

    if split_filename[-1] == 'csv':
        reader = list(csv.reader(original_data, delimiter=','))
    
    configfileName = '_'.join(get_split_filename[:-1])

    if configfileName in config.filenames.keys():
        
        file_limit_detail = config.filenames[configfileName]
        if (len(reader) > file_limit_detail['max_limit'] or len(reader) < file_limit_detail['min_limit']):
            return (False, 'File Recon check failed')
    
        return (True, 'File data limit is valid')
    return (False, 'File not found')
