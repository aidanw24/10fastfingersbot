from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login import login

def take(driver):
    driver.get("https://10fastfingers.com/typing-test/english")
    for i in range(150):
        try:
            time.sleep(0.2)
            word = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[@wordnr ={i}]"))).text
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputfield"))).send_keys(word)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputfield"))).send_keys(" ")
        except:
            pass

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(driver)
    take(driver)
    