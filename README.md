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

1. Clone the repository and enter our code directory.   
`git clone https://github.ncsu.edu/sshanbh2/TweetSmart.git`     
`cd TweetSmart/code`

2. In order to get a good number of random usernames (~10000) to perform our analysis on:       
Run:     
`python3 getUserNames.py <start_username>` 

Start_username can be any username whose connections will give us a list of 10K users. We have used 'elonmusk' for obtaining our data.


