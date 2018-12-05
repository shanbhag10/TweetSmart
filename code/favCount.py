import tweepy
import pandas as pd
import os


keys = pd.read_csv('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv')

# Authentication

def get_fav_count():
	d = {}

	for i in range(len(keys['consumer'])):
		auth = tweepy.OAuthHandler(keys['consumer'][i], keys['consumer_s'][i])
		auth.set_access_token(keys['access'][i], keys['access_s'][i])
		api = tweepy.API(auth)
		print(api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining'])

	# path1 = "/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_1.csv"

	# if os.path.isfile(path1):
	# 	file = open(path1)
	# 	for line in file:
	# 		entry = line.split(",")
	# 		print(entry[1]+" "+entry[2])
			#d[entry[0]] = entry[1]


	print(d)


			

def temp(screen_name,path):
	op = path + "/" + screen_name.strip() +".csv"
	#print(op)


if __name__ == '__main__':
	get_fav_count()
	#file = open('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard20/0.txt') 
	#users = file.readlines()
	#for user in users:
	#	temp(user,'/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/tp')



