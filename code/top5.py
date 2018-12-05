import pandas as pd
import itertools
import collections
import sys

#/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_
path = sys.argv[1].strip()
#/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/top5/top5_
op_path = sys.argv[2].strip()
number = sys.argv[3].strip()
path = path+number+'.csv'
df = pd.read_csv(path)
followList = dict()
input = dict()

# Read CSV in dict of dict
for index, row in df.iterrows():
	if row['Liker'] not in input.keys():
		input[row['Liker']]=dict()
	input[row['Liker']][row['Poster']]=row['Likes_count']

# Get top 5 elements from original list
for key, value in input.items():
	input[key] = list(itertools.islice((sorted(value.items(), key=lambda t: t[1], reverse=True)), 0, 5)) 

# Get reversed list of posters and likers who havve them in top 5
for key, value in input.items():
	for poster, likes in value:
		if poster not in followList.keys():
			followList[poster] = []
		followList[poster].append(key)
		

# Write to csv
#df = pd.DataFrame(list(d.items()),columns=['Poster','Likes_count'])
csv_dict = pd.DataFrame(list(followList.items()),columns=['Poster','Likers'])
csv_dict.to_csv(op_path+number+'.csv', header=False)

#new_data = pd.read_csv('followerList.csv', header=None)
# print(new_data)
