#links
#https://www6.whentowork.com/cgi-bin/w2wF3.dll/empschedule?SID=320330770411C&lmi=
#https://hrselfserve.info.yorku.ca/

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime

load_dotenv()
myusername = os.getenv("USERNAME")
mypassword = os.getenv("PASSWORD")
mybypasscode = os.getenv("BYPASSCODE")

w2work = "https://whentowork.com/logins.htm?_ga=2.111829773.824138766.1746351388-699864049.1701384436"
hrSelfServe = "https://hrselfserve.info.yorku.ca/"

''''''
#headles setting
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking") 
chrome_options.add_argument("--disable-notifications")  
#chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  

#chromedriver
current_directory = os.getcwd()
chromedriver_path = os.path.join(current_directory, "chromedriver")
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def open_broswer(driver, website):
    driver.get(website)

def log_into_w2w(driver, website):
    
    when2workusername = driver.find_element(By.NAME, 'UserId1')
    when2workusername.send_keys(myusername);

    when2workpassword = driver.find_element(By.NAME, 'Password1')
    when2workpassword.send_keys(mypassword);

    loginbutton = driver.find_element(By.NAME, "Submit1")
    loginbutton.click();

    myschedule = driver.find_element(By.ID, 'myschedule')
    myschedule.click();

    myshifts = driver.find_element(By.XPATH, '//*[@id="emptopnav"]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[1]')
    myshifts.click();


open_broswer(driver, w2work)
time.sleep(1)
log_into_w2w(driver, w2work)
time.sleep(10)

'''
notes for future me
-use the Myshifts tab in when2work and parse through that to get your shifts

'''