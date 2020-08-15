from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image

def save(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start-btn"))).click()
    time.sleep(0.8)
    element = driver.find_element_by_id("word-img")
    location = element.location
    size = element.size
    driver.save_screenshot("pageImage.png")
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    im = Image.open('pageImage.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save('element.png')