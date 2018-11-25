file = open('/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/final10K.txt')

temp = []
index = 1
i=0
block_size=1043

for user in file:
	i+=1
	temp.append(user)
	if i%block_size==0:
		output = '/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/shard/'+str(index) + '.txt'
		index+=1
		print(i,output)
		with open(output, 'w') as f:
			for item in temp:
				f.write(item)
		print('success')