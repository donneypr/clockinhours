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


def login_and_bypass_verification(driver, website_url, myusername, mypassword, mybypasscode):
     try:
         driver.get(website_url)
         wait = WebDriverWait(driver, 10)
         username_input = wait.until(
             EC.presence_of_element_located((By.ID, "mli"))
         )
         username_input.clear()
         username_input.send_keys(myusername)
 
         # Enter password
         password_input = driver.find_element(By.NAME, "password")
         password_input.clear()
         password_input.send_keys(mypassword)
 
         # Click login button
         log_in = driver.find_element(By.NAME, "dologin")
         log_in.click()
 
         time.sleep(5)
         print("Logged in successfully. Waiting for user action.")
 
         # Wait for verification code element
         wait = WebDriverWait(driver, 10)
         verification_code_element = wait.until(
             EC.presence_of_element_located((By.CLASS_NAME, "verification-code"))
         )
         print("Verification code content:", verification_code_element.text)
 
         time.sleep(5)
 
         # Click 'Other Options'
         other_options_button = wait.until(
             EC.element_to_be_clickable((By.CLASS_NAME, "other-options-link"))
         )
         other_options_button.click()
 
         time.sleep(1)
 
         try:
             bypass_code_link = WebDriverWait(driver, 20).until(
                 EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="test-id-bypass"]'))
             )
             bypass_code_link.click()
             print("Successfully clicked the bypass code link.")
         except Exception as e:
             print(f"An error occurred: {e}")
 
         # Enter bypass code
         bypass_code_input = wait.until(
             EC.visibility_of_element_located((By.ID, "passcode-input"))
         )
         bypass_code_input.send_keys(mybypasscode)
         print("Bypass code inputted.")
 
         try:
             verify_button = WebDriverWait(driver, 20).until(
                 EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="verify-button"]'))
             )
             verify_button.click()
             print("Successfully clicked the verify button.")
         except Exception as e:
             print(f"An error occurred while clicking the verify button: {e}")
 
         try:
             trust_browser_button = WebDriverWait(driver, 20).until(
                 EC.element_to_be_clickable((By.ID, "trust-browser-button"))
             )
             trust_browser_button.click()
             print("Successfully clicked the 'Trust Browser' button.")
         except Exception as e:
             print(f"An error occurred while clicking the button: {e}")
 
         time.sleep(10)
 
     except Exception as e:
         print(f"An error occurred during the login and verification process: {e}")


open_broswer(driver, w2work)
time.sleep(1)
log_into_w2w(driver, w2work)
time.sleep(10)

'''
notes for future me
-seems like HRSELFSERVE opens the entertime depending on the curr time, need to check this on the server
'''