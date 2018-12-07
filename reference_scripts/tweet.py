import twitter
api=twitter.Api(consumer_key='IFPYrIpyKNqt8qe7GbQvw8NzQ',consumer_secret='mo2eR5eoGLu595DaSKszFanUWcvYpTHKRIaRyvGnYHA4jUXOKi',access_token_key='779885459929337856-y0LNiqvm4EsFWDguaLW712p8e9c5MdH',access_token_secret='tvxnYaWGgTaL1cwDF0QAGBKkeBvqYBSEgzbM9GwsUqkIX')
t=api.GetFavorites(screen_name="aishwaryassr1",count=10);
tweets = [i.AsDict() for i in t]
print (tweets)
