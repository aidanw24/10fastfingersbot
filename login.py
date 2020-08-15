from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver):
    driver.get("https://10fastfingers.com/login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "UserEmail"))).send_keys("YOUREMAILHERE")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "UserPassword"))).send_keys("YOURPASSWORDHERE")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-form-submit"))).click()
    time.sleep(3)