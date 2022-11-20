from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[1])