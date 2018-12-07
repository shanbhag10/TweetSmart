import pandas as pd
import pickle
import sys

path = sys.argv[1].strip()
op_path = sys.argv[2].strip()
#/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/input_list.txt
paths = open(path)
d = {}


def saveDict():
	for path in paths:
		print(path)
		file = pd.read_csv(path.strip())
		for index, entry in file.iterrows():
			#print(entry[2])
			entry[2] = entry[2].replace("[","")
			entry[2] = entry[2].replace("'","")
			entry[2] = entry[2].replace("]","")

			entry[2] = entry[2].strip()
			entry[2] = entry[2].split(",")
			
			if entry[1] not in d:
				d[entry[1]] = []	
			d[entry[1]].extend(entry[2])
			

	df = pd.DataFrame(list(d.items()),columns=['Poster','Likers'])
	#'/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/overallTop5.csv
	df.to_csv(op_path)



# mydict = {'a': 1, 'b': 2, 'c': 3}
# output = open('myfile.pkl', 'wb')
# pickle.dump(mydict, output)
# output.close()

# # read python dict back from the file
# pkl_file = open('myfile.pkl', 'rb')
# mydict2 = pickle.load(pkl_file)
# pkl_file.close()

# print mydict
# print mydict2


if __name__ == '__main__':
	saveDict()
