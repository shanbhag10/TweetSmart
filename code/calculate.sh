for i in 1 2 3 4 5 6 7 8 9 10 11 12 13
do
	python3 top5.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/total/total_ /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/top5/top5_ $i
	python3 reduce.py /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/input_list.txt /Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/overallTop5.csv
done