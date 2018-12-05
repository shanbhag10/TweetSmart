#!/bin/sh
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13
do
  echo $i
  #python3 twitter_likes.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard750/ 1 /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_ 
  python3 twitter_likes.py /home/ubuntu/TweetSmart/data/twitter_keys.csv /home/ubuntu/TweetSmart/data/shard750/ $i /home/ubuntu/TweetSmart/data/total/total_ /home/ubuntu/TweetSmart/data/output/
  
  sleep 900
done
