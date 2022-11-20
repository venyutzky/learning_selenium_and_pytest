from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()

driver.get("https://demoqa.com/menu")
driver.maximize_window()
driver.implicitly_wait(10)

#Cara 1
menu =  driver.find_element(By.LINK_TEXT, "Main Item 2")
Hover = ActionChains(driver).move_to_element(menu)
Hover.perform()

#Cara 2
ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Main Item 3")).perform()
