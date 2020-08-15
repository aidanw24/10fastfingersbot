from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login import login
from PIL import Image
from saveimage import save
from textread import reader
from anticheat import beatanticheat
from testtaker import take

driver = webdriver.Chrome(ChromeDriverManager().install())

login(driver) # logins in

take(driver) # takes standard typing test

beatanticheat(driver) # passes anti cheat




