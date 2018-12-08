from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
import sys
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import os



uname = "saurabhtp1"
password = "Dic#1234"

total = pd.DataFrame([],columns=['Poster','Likes_count','Liker'])

def get_likes_selenium(chromepath,name,op_path):
    global total
    try:
        name = name.strip()
        print(name)
        path1 = op_path+name+".csv"
        if os.path.isfile(path1):
            return
            # file = open(path1)
            # for line in file:
            #     entry = line.split(",")
            #     if entry[2] != 'Likes_count':
            #         d[entry[1]] = int(entry[2])

        start = time.time()
        website = "https://twitter.com/"+name+"/likes"

        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        browser = webdriver.Chrome(executable_path=chromepath,chrome_options=chrome_options)
        browser.get(website) 

        d = {}
        



    #//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input
#//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input
#//*[@id="page-container"]/div/div[1]/form/div[2]/button
   

    #//*[@id="stream-item-tweet-1057307402289188871"]/div/div[2]/div[1]/a/span[2]/b
    #//*[@id="stream-item-tweet-1059491155564359688"]/div/div[2]/div[1]/a/span[2]/b
    #//*[@id="stream-item-tweet-1056221361704644608"]/div/div[2]/div[1]/a/span[2]/b
    
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'))).send_keys(uname)
        
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'))).send_keys(password)
        
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/div[2]/button'))).click()     
      
        num = browser.find_element_by_xpath("//*[@id='page-container']/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[4]/a/span[3]")

        last_height = browser.execute_script("return document.body.scrollHeight")
        count = 0
        while count < 5:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            count += 1

        ids = browser.find_elements_by_xpath("//*[contains(@id,'stream-item-tweet-')]")
        comment_ids = []
        for i in ids:
            comment_ids.append(i.get_attribute('id'))

        #users = []
        for com in comment_ids:
            username = browser.find_element_by_xpath('//*[@id="'+com+'"]/div/div[2]/div[1]/a/span[2]/b')
            #users.append(username.text)

            if username.text in d:
                d[username.text]+=1
            else:
                d[username.text]=1


        df = pd.DataFrame(list(d.items()),columns=['Poster','Likes_count'])
        length = len(df['Poster'])

        df['Liker'] = pd.Series([name]*length, index=df.index)

        op = op_path+name.strip()+".csv"
        df.to_csv(op)
    
        total = total.append(df, ignore_index=True)

        
            #print(username.text)
        print("Total Records: ",len(d))


        end = time.time()
        browser.close()
        print("Total Time: ",end - start)

    except Exception as error:
        print(error)
            
            

if __name__ == '__main__':
    path = '/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/Git/TweetSmart/data/shard750/'
    number = sys.argv[1]
    chromePath = "/Users/saurabhshanbhag/Desktop/chromedriver"
    op_path = "/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/selenium_data/"
    total_path = "/Users/saurabhshanbhag/Desktop/PROJECTS/TweetSmart/selenium_total/"

    path = path+number+'.txt'
    file = open(path) 
    users = file.readlines()
    for name in users:
        get_likes_selenium(chromePath,name,op_path)

    total.to_csv(total_path+number+'.csv');
    
    