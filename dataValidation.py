import csv
import json
import rules
import config
import logging
from io import StringIO

#Create and configure logger 
logging.basicConfig(filename="logs/data_check.log", format='%(asctime)s [%(levelname)s] %(message)s') 
  
#Creating an object
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

def old_file_row_count():
    old_file = open("old_ninad_joshi_monthly_121212.csv", "rb")
    reader_old_file = old_file.read()
    old_file_reader = list(csv.reader(StringIO(str(reader_old_file,'utf-8')), delimiter=','))
    return len(old_file_reader) - 1

def data_check(file_data, extension):
    logger.info("data check function initialized")

    #old file row check
    row_limit = old_file_row_count()

    original_data = StringIO(str(file_data,'utf-8'))
    data_dict = []
    if extension == 'csv':
        reader = list(csv.reader(original_data, delimiter=','))
        headers = reader[0]
        data_dict = [{i : row[headers.index(i)] for i in headers} for row in reader[1:]]
    
    else:
        logger.error("File has unknown extension")
        return (False, 'File has unknown extension')

    if (len(data_dict) < row_limit):
        logger.error("File has low data as expected")
        return (False, 'File has low data as expected')

    error_columns = []
    error_messages = []
    
    for index, row in enumerate(data_dict):
        for column in config.columns_rules:
            msg1 = rules.null_check(config.columns_rules[column], row[column])
            msg2 = rules.number_check(config.columns_rules[column], row[column])
            if msg1 != '' or msg2 != '':
                error_messages.append('Data Error '+ msg1 + msg2 +' in Column name:' + column + ' and Row number:' + str(index + 1))
                error_columns.append(index)

    if len(error_columns) > 0:
        logger.error('\n'.join(error_messages))
        return (False, '\n'.join(error_messages))
    
    logger.info("data check function finished")
    return (True, 'File is valid')
