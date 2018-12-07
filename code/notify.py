import sys
import pandas as pd

#/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/overallTop5.csv

path = sys.argv[1].strip()
poster = sys.argv[2].strip()

file = pd.read_csv(path.strip())
for index, entry in file.iterrows():
	if entry[1] == poster:
		entry[2] = entry[2].replace("[","")
		entry[2] = entry[2].replace("'","")
		entry[2] = entry[2].replace("]","")
		entry[2] = entry[2].replace(" ","")
		entry[2] = entry[2].rstrip()
		notif = entry[2].split(',')
		print("Notify the Following ", len(notif), " users.")
		for i in range(len(notif)):
			print("   ",i+1,notif[i])
		break