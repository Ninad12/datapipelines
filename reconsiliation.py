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

def data_check(file_data, extension):
    logger.info("data check function initialized")

    row_limit = 2
    original_data = StringIO(str(file_data,'utf-8'))
    data_dict = []
    if extension == 'csv':
        reader = list(csv.reader(original_data, delimiter=','))
        headers = reader[0]
        data_dict = [{i : row[headers.index(i)] for i in headers} for row in reader[1:]]
    
    else:
        logger.error("File has unknown extension")
        return False

    if (len(data_dict) < row_limit):
        logger.error("File has low data as expected")
        return False

    error_columns = []
    error_messages = []
    for index, row in enumerate(data_dict):
        for column in config.columns_rules:
            if not rules.null_check(config.columns_rules[column], row[column]) or not rules.number_check(config.columns_rules[column], row[column]):
                error_messages.append('Data Error in Column name:' + column + ' and Row number:' + str(index + 1))
                error_columns.append(index)

    if len(error_columns) > 0:
        logger.error('\n'.join(error_messages))
        return False
    
    logger.info("data check function finished")
    return True
