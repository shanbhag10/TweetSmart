sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install boto3
pip3 install pandas
pip3 install tweepy
pip3 install flask
pip3 install ansible
pip3 install selenium
cd /tmp/
wget -q -O - "https://dl-ssl.google.com/linux/linux_signing_key.pub" | sudo apt-key add -
sudo sed -i '$ a deb http://dl.google.com/linux/chrome/deb/ stable main' /etc/apt/sources.list
sudo apt-get update
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install xvfb
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
sudo apt-get -y install unzip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
mkdir /home/ubuntu/TweetSmart/selenium_data
mkdir /home/ubuntu/TweetSmart/selenium_total

#