import os
import sys
import logging
#import rds_config
import pymysql
print(os.environ)
if 'RDS_HOSTNAME' in os.environ:
    print "hello"
    DATABASES = {
        'default': {
            'ENGINE': 'Aurora MySQL 5.6.10a',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn=pymysql.connect(os.environ['RDS_HOSTNAME'],user=os.environ['RDS_USERNAME'],passwd=os.environ['RDS_PASSWORD'],db=os.environ['RDS_DB_NAME'],connect_timeout=10)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()	
item_count = 0
filename="C:/Users/Aishwarya/tweet/TweetSmart/data/total/total_1.csv"
with conn.cursor() as cur:
    print("yaaay")
    #cur.execute("create table Employee3 (EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
    #cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
    #cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
    #cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
    cur.execute('SET GLOBAL local_infile = true;')
    cur.execute('LOAD DATA LOCAL INFILE %s INTO TABLE top;',(filename))
    conn.commit()
    cur.execute("select * from Employee3")
    for row in cur:
        item_count += 1
        logger.info(row)
print("Added %d items to RDS MySQL table" %(item_count))
	