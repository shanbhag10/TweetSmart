import tweepy

# Twitter API credentials
consumer_key = ['IFPYrIpyKNqt8qe7GbQvw8NzQ','mgf6yCpEQI7BBI1AXMP0F1qZA','ujn2X5xT7Q4LyVCCJfgyRXHqG']
consumer_secret = ['mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi','2aYhS9197XivXUhsFpILSM1MJFLIQi6FNUQvNO2Nw51lLFLPfx','nLUy8BlHwB3kWvLToJut286iZl2IQSY52H0znGozwbFwKkOWtk']
access_key = ['779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH','930245742412877824-yh94Uu5E6yihujnWa2rzWnCU4bnosZK','1067674130856714241-tLRIGgNuiBc1Og04byzfk2wBHACnmh']
access_secret = ['tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX','RKFgSwp6BZ05KTvJfVo6p4M9cwA8u6OJOJ5qWPEKKG3wq','tSkrl2rGff7wzZWhF4OsQYx8FZYG40I5BvNOsTqSzAZjF']

# Authentication

def get_fav_count():
	for i in range(len(consumer_key)):
		auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret[i])
		auth.set_access_token(access_key[i], access_secret[i])
		api = tweepy.API(auth)
		if (api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining']) == 0:
			print('yess')

if __name__ == '__main__':
	get_fav_count()



