import os
import sys

csv_header = ',Poster,Likes_count,Liker'
num = sys.argv[1]
csv_out = '/home/ubuntu/TweetSmart/selenium_total/total_'+num+'.csv'

csv_dir = '/home/ubuntu/TweetSmart/selenium_data/'

dir_tree = os.walk(csv_dir)

for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(csv_dir+file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

for file in csv_list:
   csv_in = open(file)
   for line in csv_in:
      if line.startswith(csv_header):
         continue
      csv_merge.write(line)
   csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)