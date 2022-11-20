from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

#by ID
#driver.find_element(By.ID, "username").send_keys("realmeownub")

#by Name
#driver.find_element(By.NAME, "password").send_keys("uno123")

#untuk klik link yang full caption
#driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()

#untuk klik link yang sebagian dan terdapat kata tersebut
#driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()

#by Tag Name
#link = driver.find_elements(By.TAG_NAME, "a")
#print(len(link))

#by Class
#driver.find_element(By.CLASS_NAME, "radius").click()

time.sleep(3)

#by CSS Selector
#driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()

#by Xpath
driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

#driver.quit()
