import tweepy
import csv
import time
import pandas as pd
import heapq 
# Twitter API credentials
consumer_key = 'IFPYrIpyKNqt8qe7GbQvw8NzQ'
consumer_secret = 'mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi'
access_key = '779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH'
access_secret = 'tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
users = tweepy.Cursor(api.followers, screen_name="kevinolearytv",count=1000).items()
for user in users:
 print(user.screen_name)
