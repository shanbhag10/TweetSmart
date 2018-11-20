import tweepy
import sys

# Twitter API credentials
consumer_key = 'IFPYrIpyKNqt8qe7GbQvw8NzQ'
consumer_secret = 'mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi'
access_key = '779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH'
access_secret = 'tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def getInitialUserNames(screen_name,users):
	print("Getting initial usernames")
	for page in tweepy.Cursor(api.favorites,id=screen_name,wait_on_rate_limit=True, count=200).pages(200):
		for status in page:
			users.add(status.user.screen_name)

	with open('initial.txt', 'w') as f:
		for item in users:
			f.write("%s\n" % item)

	print("initial usernames ready. File size = ",len(users))



def getFinalUserNames(screen_name,users,count):
	for page in tweepy.Cursor(api.favorites,id=screen_name,wait_on_rate_limit=True, count=200).pages(200):
		for status in page:
			users.add(status.user.screen_name)
			count += 1
			if count % 50 == 0:
				print("Parsed ",count," usernames")
				print("Added ",len(users)," usernames")
			


if __name__ == '__main__':
	username = sys.argv[1]
	users = {username}
	count = 0
	getInitialUserNames(username,users)
	file = open("initial.txt", "r")
	listOfUsernames = file.readlines()
	print("Getting final usernames")
	for usname in listOfUsernames:
		if len(users) < 10000:
			getFinalUserNames(usname,users,count)
		else:
			break

	print(len(users))

	with open('final10K.txt', 'w') as f:
		for item in users:
			f.write("%s\n" % item)

	print("10K Usernames file ready")

	


