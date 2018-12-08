sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install boto3
pip3 install pandas
pip3 install tweepy
pip3 install flask
pip3 install selenium
cd /tmp
wget -q -O - "https://dl-ssl.google.com/linux/linux_signing_key.pub" | sudo apt-key add -
sudo vim /etc/apt/sources.list

