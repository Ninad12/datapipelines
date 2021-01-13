
import boto3
import urllib
import json
import datetime
import uuid

client = boto3.client('stepfunctions')

print ('Loading Function...')

def lambda_handler(event, context):

    print ("New file has arrived")
    
    FileName = event['Records'][0]['s3']['object']['key']
    print (FileName)
    
    BucketName = event['Records'][0]['s3']['bucket']['name']
    print (BucketName)
    
    transactionId = str(uuid.uuid1())
    input = {'FileName':FileName, 'BucketName':BucketName}
    
    response = client.start_execution(
        stateMachineArn = 'arn:aws:states:us-west-1:764002460229:stateMachine:FileValidationStateMachine',
        name = transactionId,
        input = json.dumps(input)
        )
        
    print (input)
    print ('Function Executed...')
