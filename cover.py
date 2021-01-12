file_data = open('HSBC_Volumes_monthly_121212.csv',"rb")
read_data = file_data.read()
import datavalidation as dv

dv.data_check(read_data,'csv')

