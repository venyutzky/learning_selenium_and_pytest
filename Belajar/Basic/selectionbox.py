from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import pyautogui
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/select-menu")


#old Style selection
pilih =  Select(driver.find_element(By.ID, "oldSelectMenu"))
time.sleep(2)
pilih.select_by_visible_text("Voilet")
time.sleep(1)
pilih.select_by_value('10')

time.sleep(1)

#select one with typing
driver.find_element(By.XPATH, '//*[@id="selectOne"]/div/div[1]/div[1]').click()
time.sleep(1)
pyautogui.typewrite("Prof.")
time.sleep(1)
pyautogui.press("enter")