sudo apt-get update
sudo apt-get -y install google-chrome-stable
sudo apt-get -y install xvfb
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver