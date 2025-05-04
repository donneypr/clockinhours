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
    driver.get(website)

    when2workusername = driver.find_element(By.NAME, 'UserId1')
    when2workusername.send_keys(myusername)

    when2workpassword = driver.find_element(By.NAME, 'Password1')
    when2workpassword.send_keys(mypassword)

    loginbutton = driver.find_element(By.NAME, "Submit1")
    loginbutton.click()

    myschedule = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'myschedule'))
    )
    myschedule.click()

    myshifts = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="emptopnav"]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[1]'))
    )
    myshifts.click()

    schedule_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "underline"))
    )

    tbody = schedule_table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        td_list = row.find_elements(By.XPATH, ".//td[@colspan='2']")
        if not td_list:
            continue  

        td = td_list[0]
        nobrs = td.find_elements(By.TAG_NAME, "nobr")

        if len(nobrs) >= 2:
            date_text = nobrs[0].text.strip()
            time_text = nobrs[1].text.strip()

            print("Date:", date_text)
            print("Time:", time_text)
            print("-----------------------")


open_broswer(driver, w2work)
time.sleep(1)
log_into_w2w(driver, w2work)
time.sleep(10)

'''
notes for future me
-use the Myshifts tab in when2work and parse through that to get your shifts

'''