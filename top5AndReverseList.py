import pandas as pd
import itertools
import collections

df = pd.read_csv('Test1.csv')
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
    if poster in followList.keys():
      followList[poster].append(key)
    else:
      followList[poster] = [key]

# Write to csv
csv_dict = pd.DataFrame.from_dict(followList, orient="index")
csv_dict.to_csv('file1.csv', header=False)

new_data = pd.read_csv('followerList.csv', header=None)
# print(new_data)
