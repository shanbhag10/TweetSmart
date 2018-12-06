#!/usr/bin/env python3
import boto3
import pandas as pd

ec2 = boto3.resource('ec2')
instance_list = []
for instance in ec2.instances.all():
    instance_list.append((instance.id,instance.public_dns_name,instance.state,instance.public_ip_address))
    #inputfile+=1
    
instance_df = pd.DataFrame(instance_list)
instance_df.to_csv('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/instances.csv', index=True, header=True)
print(instance_df)
   