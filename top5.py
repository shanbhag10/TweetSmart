import pandas as pd
import itertools
import collections
df = pd.read_csv('Test1.csv')
input = dict()

# Read CSV in dict of dict
for index, row in df.iterrows():
  if row['Liker'] not in input.keys():
    input[row['Liker']]=dict()
  input[row['Liker']][row['Poster']]=row['Likes_count']
  
# Get top 5 elements from original list
for key, value in input.items():
  input[key] = list(itertools.islice((sorted(value.items(), key=lambda t: t[1], reverse=True)), 0, 5)) 
  
print(input)
