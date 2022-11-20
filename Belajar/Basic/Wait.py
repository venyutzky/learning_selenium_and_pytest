from selenium import webdriver
from selenium.webdriver.common.by import By

## library tambahan untuk explicitly wait ###
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# -------------------
driver = webdriver.Chrome()

#### Implicitly Wait ####
#driver.implicitly_wait(10)
#driver.get("https://demoqa.com/alerts")
#driver.get("https://demoqa.com/books")
#driver.find_element(By.ID, "login").click()


#### Explicitly Wait ####
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "timerAlertButton").click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert diklik")

except TimeoutException:
    print("Alert tidak muncul")
    pass