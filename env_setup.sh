sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install boto3
pip3 install pandas
pip3 install tweepy
pip3 install flask
pip3 install selenium
cd /tmp
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install xvfb
curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome