import csv
import json
import dataValidationRules as rules
import dataValidationConfig as config
import logging
from io import StringIO
from datetime import datetime
import shutil
import os



now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H:%M:%S")
logFileName = "logFile_dataValidation_"+dt_string+".txt"
logFilePath = "logs/"+logFileName

shutil.rmtree('logs')
os.mkdir('logs')
logFile = open(logFilePath, "x")

#Create and configure logger 
logging.basicConfig(filename="logs/"+logFileName, format='%(levelname)s:%(message)s', level=logging.DEBUG)
  
#Creating an object
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
#logger.setLevel(logging.DEBUG)

def data_check(file_data, extension):
    logger.info("data check function initialized")

    original_data = StringIO(str(file_data,'utf-8'))
    data_dict = []
    if extension == 'csv':
        reader = list(csv.reader(original_data, delimiter=','))
        headers = reader[0]
        data_dict = [{i : row[headers.index(i)] for i in headers} for row in reader[1:]]
    
    else:
        logger.error("File has unknown extension")
        return (False, 'File has unknown extension')

    error_columns = []
    error_messages = []
    
    for index, row in enumerate(data_dict):
        for column in config.columns_rules:
            null_check = rules.null_check(config.columns_rules[column], row[column])
            number_check = rules.number_check(config.columns_rules[column], row[column])
            if null_check != '':
                error_messages.append('Data Error '+ null_check +' in Column name:' + column + ' and Row number:' + str(index + 1))
                error_columns.append(index)
            if number_check != '':
                error_messages.append('Data Error '+ number_check +' in Column name:' + column + ' and Row number:' + str(index + 1))
                error_columns.append(index)

    if len(error_columns) > 0:
        logger.error('\n'.join(error_messages))
        return(False,'\n'.join(error_messages))
        

    
    response = 'File is valid'
    logger.info(response)
    logger.info("data check function finished")
    return (True,response)
