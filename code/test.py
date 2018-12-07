import tweepy
#import csv
import ast
import os
import random
import boto3
import sys
import pandas as pd

likes = []
err = -1
total = pd.DataFrame([],columns=['Poster','Likes_count','Liker'])


def get_all_tweets(screen_name):
	
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		#print("...%s tweets downloaded so far" % (len(alltweets)))
		outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
		print(outtweets)
	
def getLikes(screen_name):
	for page in tweepy.Cursor(api.favorites,id=screen_name,wait_on_rate_limit=True, count=200).pages(200):
		for status in page:
			likes.append((screen_name,status.user.screen_name,status.created_at))


def getLikesCount(screen_name,op_path):
	global err
	global total
	try:
		d = {}
		screen_name = screen_name.strip()
		print("Username: ",screen_name)

		path1 = op_path+screen_name+"1.csv"

		if os.path.isfile(path1):
			file = open(path1)
			for line in file:
				entry = line.split(",")
				if entry[2] != 'Likes_count':
					d[entry[1]] = int(entry[2])

		print(d)

		likes = api.favorites(screen_name = screen_name)
		for like in likes:
			if like.user.screen_name in d:
				
				d[like.user.screen_name]+=1
			else:
				d[like.user.screen_name]=7

		df = pd.DataFrame(list(d.items()),columns=['Poster','Likes_count'])
		length = len(df['Poster'])

		df['Liker'] = pd.Series([screen_name]*length, index=df.index)
		op = op_path+screen_name.strip()+"1.csv"
		df.to_csv(op)

		total = total.append(df, ignore_index=True)
		err = 0
	except Exception as error:
		err = 1
		print(error)




if __name__ == '__main__':
	#/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv
	keys = pd.read_csv('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv')
	op_path = '/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/output/'
	i = 9
	user = 'Shanbhagsaurabh'

	auth = tweepy.OAuthHandler(keys['consumer'][i], keys['consumer_s'][i])
	auth.set_access_token(keys['access'][i], keys['access_s'][i])
	api = tweepy.API(auth)

	#total = pd.read_csv('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_13.csv')
	while err != 0:
		getLikesCount(user,op_path)
	total.to_csv('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_14.csv')
	print("COMPLETE")
	
	

