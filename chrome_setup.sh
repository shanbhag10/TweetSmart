sudo apt-get update
cd /tmp/
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install xvfb
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
sudo apt-get -y install unzip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
mkdir /home/ubuntu/TweetSmart/selenium_data
mkdir /home/ubuntu/TweetSmart/selenium_total
