import boto3
import datetime
import csv

s3 = boto3.client('s3')
def lambda_handler(event, context):
    
    print ("Received message from STEP Function")
    print ("File Writing function initiated")
    print (event)
    
    BucketName = event['BucketName']
    FileName = event['FileName']
    Body = event['Body']
    
    print (FileName)
    print (BucketName)
    print (Body)
    
    upload_file_bucket = 's3datastage'
    upload_file_key = 'out_'+FileName
    
    print (upload_file_bucket)
    print (upload_file_key)
    
    TEMP_FILENAME = "/tmp/test.csv"
   
    with open(TEMP_FILENAME,"w") as f:
        csvwriter = csv.writer(f)
        header = True
        first_page = True
        
        csvreader = csv.reader(Body.splitlines(),delimiter=',')
        #next(reader)
        for row in csvreader:
            csvwriter.writerow(row)
            print (row)

    
    s3.upload_file(TEMP_FILENAME, upload_file_bucket, upload_file_key)
    
    print ('PUT Complete')
    
    resp = s3.get_object(Bucket=upload_file_bucket, Key=upload_file_key)
    data = resp['Body'].read().decode("utf8")
    print (data)
    
    response = {}
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = 'Hello from FileWriter'
    #response['Body'] = Body
    
    print (response)
    
    print ("Function executed")
    
    return response  