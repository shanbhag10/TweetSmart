# TweetSmart

### Smart Notification System for Twitter using Data Intensive Computing and Distributed Storage.

TweetSmart is a data-intensive computing system for dynamically determining the top 5
interests of each user and notifying them about the most recent updates regarding those
interests. We will be building a data intensive solution which will store the historical as well as
streaming data and we will query this distributed database to calculate those interest values with
a few parameters. TweetSmart will notify the users only about the updates of interest for them.
The data-store will contain terabytes of historical data along with high velocity streaming data.
This framework will help to analyze topics of interest over time, locations, age of users, etc. and
enable smarter targeting of advertisements.


## Running Instructions

Note: Please change the twitter_keys.csv file with your own Twitter Developer API access tokens. Also, please change the absolute paths to the directories to your own paths. 

1. **Initialize:**   
Clone the repository and enter our code directory.   
`git clone https://github.ncsu.edu/sshanbh2/TweetSmart.git`     
`cd TweetSmart/code`

2. **Gather Usernames**    
We need a good number of *random* usernames (~10000) to perform our analysis on: 
Run:     
`python3 getUserNames.py <start_username>`    
*Start_username can be any username whose connections will give us a list of 10K users. We have used 'elonmusk' for obtaining our data.*

3. **Sharding data**  
We have made 13 shards of 750 usernames each which gave us 9750 usernames in total. We would have more shards if we have more usernames.    
Run:    
`python3 shard.py <shard_size>`  
*We have used block size = 750*

4. **Getting likes count (Mapper 1)**    
We now need to get likes of each user from Twitter_Favorites_list API and counting the number of likes for each particular user.   
Run:   
`python3 twitter_likes.py <shard_number>`

5. **Calculating Top 5 (Mapper 2):**    
Now, we need to reverse map the likes to find out the top interests of each user. Hence, we check the top 5 likes count for each user from the output of Mapper 1 and reverse map the user to the poster so that we know that the particular user should be notified when the poster posts any content.   
Run:   
`python3 top5.py <shard_number>`

6. **Combine (Reduce):**
We need to combine the outputs of all shards as same poster might be present in multiple shards. This script takes care of combining results into one reduced output.   
Run:   
`python3 reduce.py`   

Using the output of reduce.py, we can figure out who all should be notified when one particular user posts some content.
