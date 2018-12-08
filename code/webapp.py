from flask import Flask, request, render_template

import sys
import pandas as pd


app = Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
	length=0
	if request.method == 'POST':
		username = request.form['username']
		followers = notify(username)
		length = len(followers)
		if len(followers) != 0:
			return render_template('notif.html',username=username,followers=followers,length=length)
	return render_template('notif.html',username=username,length=length)

def notify(username):
	path = '/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/overallTop5.csv'
	file = pd.read_csv(path.strip())
	for index, entry in file.iterrows():
		if entry[1].lower() == username.lower():
			entry[2] = entry[2].replace("[","")
			entry[2] = entry[2].replace("'","")
			entry[2] = entry[2].replace("]","")
			entry[2] = entry[2].replace(" ","")
			entry[2] = entry[2].rstrip()
			return entry[2].split(',')
	return []
			
if __name__ == "__main__":		
	app.run(debug=True)


