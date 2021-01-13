import csv
import json
import logging
import fileReconConfig as config
from io import StringIO
from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H:%M:%S")
logFileName = "logFile_dataRecon_"+dt_string+".txt"
logFilePath = "logs/"+logFileName

logFile = open(logFilePath, "x")

#Create and configure logger 
logging.basicConfig(filename="logs/"+logFileName, format='%(levelname)s:%(message)s', level=logging.DEBUG)
  
#Creating an object
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

def old_file_row_count():
    old_file = open("HSBC_Volumes_monthly_112020.csv", "rb")
    reader_old_file = old_file.read()
    old_file_reader = list(csv.reader(StringIO(str(reader_old_file,'utf-8')), delimiter=','))
    return len(old_file_reader) - 1

def data_check(file_data, extension):
    logger.info("data check function initialized")

    #old file row check
    row_limit = old_file_row_count()
    print (row_limit)
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
        logger.error("Check file")
        return (False, 'Check file')


    logger.info("data check function finished")
    return (True, 'File is valid')
