from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

driver.maximize_window()
time.sleep(2)
driver.minimize_window()