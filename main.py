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

w2Work = "https://www6.whentowork.com/cgi-bin/w2wF3.dll/empschedule?SID=320330770411C&lmi="
hrSelfServe = "https://hrselfserve.info.yorku.ca/"

#headles setting
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking") 
chrome_options.add_argument("--disable-notifications")  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  

#chromedriver
current_directory = os.getcwd()
chromedriver_path = os.path.join(current_directory, "chromedriver")
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def open_broswer(driver, website):
    driver.get(website)

def login_and_bypass_verification(driver, website_url, myusername, mypassword, mybypasscode):
    try:
        # Navigate to the website
        driver.get(website_url)
        # Enter username
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

        # Click 'Bypass Code' link
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

        # Click verify button
        try:
            verify_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="verify-button"]'))
            )
            verify_button.click()
            print("Successfully clicked the verify button.")
        except Exception as e:
            print(f"An error occurred while clicking the verify button: {e}")

        # Click 'Trust Browser' button
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
