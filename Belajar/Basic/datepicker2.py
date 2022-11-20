from pickletools import pyunicode
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demoqa.com/date-picker")
#driver.find_element(By.ID, "datePickerMonthYearInput").clear()

driver.find_element(By.ID, "datePickerMonthYearInput").click()
time.sleep(2)
pyautogui.press("backspace", presses=10)
time.sleep(2)
driver.find_element(By.ID, "datePickerMonthYearInput").send_keys("02/01/2022")
time.sleep(1)
pyautogui.press("enter")
