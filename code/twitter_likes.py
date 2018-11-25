import tweepy
#import csv
import boto3
import pandas as pd
#import heapq 

# Twitter API credentials
consumer_key = 'IFPYrIpyKNqt8qe7GbQvw8NzQ'
consumer_secret = 'mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi'
access_key = '779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH'
access_secret = 'tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

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
	

def getFavs(screen_name):

	likes = api.favorites(screen_name = screen_name)
	
	for like in likes:
    # Process a single status
	    
	    print("Username : ",like.user.screen_name)
	    print("Post : ",like.text)

	   #id,text,screen_name

def getLikesCount(screen_name):
	global total
	for page in tweepy.Cursor(api.favorites,id=screen_name,wait_on_rate_limit=True, count=200).pages(200):
		for status in page:
			if status.user.screen_name in d:
				d[status.user.screen_name]+=1

				#if d['name'][status.user.screen_name] > max:
				#	name = status.user.screen_name
				#	max = d['name'][status.user.screen_name]
			#d['tweet'].append(status.text)
			else:
				d[status.user.screen_name]=1


	df = pd.DataFrame(list(d.items()),columns=['Poster','Likes_count'])
	#df_count = pd.DataFrame.from_dict(d['name'])
	length = len(df['Poster'])


	df['Liker'] = pd.Series([screen_name]*length, index=df.index)
	#print(df)
	total = total.append(df, ignore_index=True)
	#df.to_csv('mattGlanz.csv')
	#sorted_by_value = sorted(d['name'].items(), key=lambda kv: kv[1])
	#sorted_by_value.reverse()
	#print(sorted_by_value)


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


if __name__ == '__main__':
	#get_all_tweets("nawalsanchit")
	users = readData('ShardedData/1.txt')
	
	#temp = ["MattGlantz","elonmusk","nawalsanchit"]
	#for user in temp:
	for user in users.iterrows():
		print(user)
		getLikesCount(user)

	print("COMPLETE")
	total.to_csv('output1.csv')

