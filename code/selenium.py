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


uname = "saurabhtp1"
password = "Dic#1234"


def get_likes_selenium(chromepath,name):
    start = time.time()
    website = "https://twitter.com/"+name+"/likes"

    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chromepath)
    browser.get(website)  
    #//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input
#//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input
#//*[@id="page-container"]/div/div[1]/form/div[2]/button
   

    #//*[@id="stream-item-tweet-1057307402289188871"]/div/div[2]/div[1]/a/span[2]/b
    #//*[@id="stream-item-tweet-1059491155564359688"]/div/div[2]/div[1]/a/span[2]/b
    #//*[@id="stream-item-tweet-1056221361704644608"]/div/div[2]/div[1]/a/span[2]/b
    try:
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'))).send_keys(uname)
        
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'))).send_keys(password)
        
        wait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/div[2]/button'))).click()     
      
        last_height = browser.execute_script("return document.body.scrollHeight")

        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(0.5)

            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                ids = browser.find_elements_by_xpath("//*[contains(@id,'stream-item-tweet-')]")
                comment_ids = []
                for i in ids:
                    comment_ids.append(i.get_attribute('id'))

                users = []
                for com in comment_ids:
                    username = browser.find_element_by_xpath('//*[@id="'+com+'"]/div/div[2]/div[1]/a/span[2]/b')
                    users.append(username.text)
                    #print(username.text)
                
                with open(name+'.txt', 'w') as f:
                    for item in users:
                        f.write("%s\n" % item)

                break
            last_height = new_height

            end = time.time()
            print("Total Records: ",len(users))
            print("Total Time: ",end - start)

    except Exception as error:
        print(error)
            
            

if __name__ == '__main__':
    name = sys.argv[1]
    chromePath = "/Users/saurabhshanbhag/Desktop/chromedriver"
    get_likes_selenium(chromePath,name)
    
    