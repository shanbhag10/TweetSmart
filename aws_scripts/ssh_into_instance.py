#!/usr/bin/env python3

import boto3
import botocore
#import boto
import paramiko

user_name='ubuntu'
instance_id='i-0defd071031a578c8'
pem_addr='/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/test/NEWKP.pem' 
aws_region='us-east-2'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file(pem_addr)
    
    print('Starting ssh connection')
    ssh.connect('ec2-3-16-156-190.us-east-2.compute.amazonaws.com',username='ubuntu',pkey=privkey)
    print('Connected')
    stdin, stdout, stderr = ssh.exec_command('cd TweetSmart/code/ && python3 twitter_likes.py')
    stdin.flush()

    data = stdout.read().splitlines()
    for line in data:
        x = line.decode()
        print(x)
    
    ssh.close()
except Exception as e:
	print(e)

'''
# Method 3
import boto3
import paramiko

user_name='ubuntu'
instance_id='i-0defd071031a578c8' #just an example
pem_addr='/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/test/NEWKP.pem' # folder path to aws instance key
aws_region='us-east-2' 

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


for instance in instances:
    if (instance.id==instance_id):
        p2_instance=instance
        break;


print('1')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
privkey = paramiko.RSAKey.from_private_key_file(pem_addr)
print(p2_instance.public_dns_name)
ssh.connect(p2_instance.public_dns_name,username=user_name,pkey=privkey)
print('3')

cmd_to_run='git clone https://github.ncsu.edu/sshanbh2/TweetSmart.git && cd TweetSmart/code && python3 twitter_likes.py' #you can seperate two shell commands by && or ;
stdin4, stdout4, stderr4 = ssh.exec_command(cmd_to_run,timeout=None, get_pty=False)

data = stdout4.read().splitlines()
print(data)
for line in data:
    x = line.decode()
        #print(line.decode())
    print(x)

ssh.close()'''


# Method 1

'''import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file("/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/keypairAWS/tweetSmart.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname="13.58.134.75", username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command("git clone https://github.ncsu.edu/sshanbh2/TweetSmart.git")
    print(stdout.read())

    # close the client connection once the job is done
    client.close()
    break



except Exception:
    print("Error")'''


# Method 2

