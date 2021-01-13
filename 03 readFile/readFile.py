import csv
import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):

    print ("Received message from STEP Function")
    print ("File Reading function initiated")
    print (event)
    
    BucketName = event['BucketName']
    FileName = event['FileName']
    
    print (FileName)
    print (BucketName)
    
    resp = s3.get_object(Bucket=BucketName, Key=FileName)
    data = resp['Body'].read().decode("utf8")
    print (data)
    

    response = {}
    response['FileName'] = FileName
    response['BucketName'] = BucketName
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = 'Hello from FileReader'
    response['Body'] = data
    
    print (response)
    
    print ("Function executed")
    
    return response
    

    

