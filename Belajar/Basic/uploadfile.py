from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver  = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#### Case button jenis input ####
#driver.get("https://demoqa.com/upload-download")

#driver.find_element(By.ID, "uploadFile").send_keys("C:/Users/Reyhan Venyutzky/Belajar Selenium/dummy.pdf")

##### Case button aja ####
driver.get("https://gofile.io/uploadFiles")

#driver.find_element(By.XPATH, '//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').send_keys(":/Users/Reyhan Venyutzky/Belajar Selenium/dummy.pdf")

driver.find_element(By.XPATH, '//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()
time.sleep(3)
pyautogui.write(r"C:\Users\Reyhan Venyutzky\Belajar Selenium\dummy.pdf")
time.sleep(2)
pyautogui.press("enter")