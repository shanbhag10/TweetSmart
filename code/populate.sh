#!/bin/sh
while true;
do
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13
	do
  		echo $i
  		#python3 twitter_likes.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/twitter_keys.csv /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard750/ $i /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_ /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/output
  		python3 twitter_likes.py /home/ubuntu/TweetSmart/data/twitter_keys.csv /home/ubuntu/TweetSmart/data/shard750/ $i /home/ubuntu/TweetSmart/data/total/total_ /home/ubuntu/TweetSmart/data/output/
  		#python3 top5.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_ /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/top5/top5_ $i
		python3 top5.py /home/ubuntu/TweetSmart/data/total/total_ /home/ubuntu/TweetSmart/data/top5/top5_ $i
		
		sleep 900
	done
	#python3 reduce.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/input_list.txt /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/overallTop5.csv
  	python3 reduce.py /home/ubuntu/TweetSmart/data/input_list.txt /home/ubuntu/TweetSmart/data/overallTop5.csv
  		
done