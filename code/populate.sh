#!/bin/sh
for i in {1..13}
do
  echo $i
  #python3 twitter_likes.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard750/ 1 /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_
  python3 twitter_likes.py /home/ubuntu/TweetSmart/data/twitter_keys.csv /home/ubuntu/TweetSmart/data/shard750/ $i /home/ubuntu/TweetSmart/data/total/total_
  
  sleep 900
done
