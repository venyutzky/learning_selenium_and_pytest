from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#### Part 1 - satu button #####

#driver.get("https://demoqa.com/alerts")
#time.sleep(2)
#driver.find_element(By.ID, "alertButton").click()
#time.sleep(2)
#driver.switch_to.alert.accept()


#### Part 2 - dua button ####
driver.get("https://demoqa.com/alerts")
time.sleep(2)

driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

driver.switch_to.alert.dismiss()

#### Part 3 - with Prompt #####

# driver.get("https://demoqa.com/alerts")
# time.sleep(2)

# driver.find_element(By.ID, "promtButton").click()

# driver.switch_to.alert.send_keys("Saya sedang test")
# time.sleep(2)
# driver.switch_to.alert.accept()
