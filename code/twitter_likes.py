import tweepy
#import csv
import boto3
import sys
import pandas as pd
#import heapq 

# Twitter API credentials


likes = []
d = {}
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

def readData(key):
	
	client = boto3.client('s3') 

	resource = boto3.resource('s3') 
	my_bucket = resource.Bucket('users10k') 

	obj = client.get_object(Bucket='users10k', Key=key)	
	users = pd.read_csv(obj['Body'])
	
	return users

def getFavs(screen_name):

	likes = api.favorites(screen_name = screen_name)
	
	for like in likes:
    # Process a single status
	    
	    print("Username : ",like.user.screen_name)
	    print("Post : ",like.text)

	   #id,text,screen_name

def getLikesCount(screen_name,path):

	global total
	print("Username: ",screen_name)
	for page in tweepy.Cursor(api.favorites,id=screen_name,wait_on_rate_limit=True, count=200).pages(200):
		for status in page:
			if status.user.screen_name in d:
				d[status.user.screen_name]+=1
			else:
				d[status.user.screen_name]=1


	df = pd.DataFrame(list(d.items()),columns=['Poster','Likes_count'])
	#df_count = pd.DataFrame.from_dict(d['name'])
	length = len(df['Poster'])


	df['Liker'] = pd.Series([screen_name]*length, index=df.index)
	df.to_csv(path+screen_name+'.csv')
	#print(df)
	total = total.append(df, ignore_index=True)


	#df.to_csv('mattGlanz.csv')
	#sorted_by_value = sorted(d['name'].items(), key=lambda kv: kv[1])
	#sorted_by_value.reverse()
	#print(sorted_by_value)

			#mid
				#if d['name'][status.user.screen_name] > max:
				#	name = status.user.screen_name
				#	max = d['name'][status.user.screen_name]
			#d['tweet'].append(status.text)




if __name__ == '__main__':
	#get_all_tweets("nawalsanchit")
	#file = open(sys.argv[1])
	consumer_key = ['IFPYrIpyKNqt8qe7GbQvw8NzQ','mgf6yCpEQI7BBI1AXMP0F1qZA','ujn2X5xT7Q4LyVCCJfgyRXHqG']
	consumer_secret = ['mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi','2aYhS9197XivXUhsFpILSM1MJFLIQi6FNUQvNO2Nw51lLFLPfx','nLUy8BlHwB3kWvLToJut286iZl2IQSY52H0znGozwbFwKkOWtk']
	access_key = ['779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH','930245742412877824-yh94Uu5E6yihujnWa2rzWnCU4bnosZK','1067674130856714241-tLRIGgNuiBc1Og04byzfk2wBHACnmh']
	access_secret = ['tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX','RKFgSwp6BZ05KTvJfVo6p4M9cwA8u6OJOJ5qWPEKKG3wq','tSkrl2rGff7wzZWhF4OsQYx8FZYG40I5BvNOsTqSzAZjF']

# Authentication
	auth = tweepy.OAuthHandler(consumer_key[0], consumer_secret[0])
	auth.set_access_token(access_key[0], access_secret[0])
	api = tweepy.API(auth)

	file = open(sys.argv[1]) 
	users = file.readlines()
	i = 0
	count = 0
	#temp = ["nawalsanchit","elonmusk","ShabeRaven"]
	#if api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining'] == 0:

	for user in users:
	#for user in users.iterrows():
		print("Remaining : ",api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining'])
		getLikesCount(user,sys.argv[2])
		count+=1
		print("Count : ",count)
		if (api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining']) == 75:
			i+=1
			if i == len(consumer_key):
				total.to_csv('output_test.csv')
				print(total)
				break
			auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret[i])
			auth.set_access_token(access_key[i], access_secret[i])
			api = tweepy.API(auth)
		
		

	print("COMPLETE")
	
	

