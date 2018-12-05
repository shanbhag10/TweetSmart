import sys

file = open('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/usernames/final10K.txt')

temp = []
index = 1
i=0
block_size=int(sys.argv[1])

for user in file:
	i+=1
	temp.append(user)
	if i%block_size==0:
		output = '/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard750/'+str(index) + '.txt'
		index+=1
		print(i,output)
		with open(output, 'w') as f:
			for item in temp:
				f.write(item)
		temp=[]
		print('success')
