from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from saveimage import save
from textread import reader
from login import login

def beatanticheat(driver):
    driver.get("https://10fastfingers.com/anticheat/view/1/1")
    save(driver)
    words = reader()
    length = len(words)
    for i in range(length):
        time.sleep(0.2)
        if i < (length - 1):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "word-input"))).send_keys(words[i] + " ")
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "word-input"))).send_keys(words[i])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit-anticheat"))).click()

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(driver)
    beatanticheat(driver)