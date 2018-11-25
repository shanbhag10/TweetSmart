import boto3
import pandas as pd

client = boto3.client('s3') 

resource = boto3.resource('s3') 
my_bucket = resource.Bucket('users10k') 

obj = client.get_object(Bucket='users10k', Key='final10K.txt')	
users = pd.read_csv(obj['Body'])

block_size = 1000
	
print(users)