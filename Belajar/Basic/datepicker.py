from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")
time.sleep(1)
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="content"]/iframe'))
#driver.find_element(By.ID, "datepicker").click()
#time.sleep(1)
#driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[5]/a').click()


#### Cara kedua ####
driver.find_element(By.ID, "datepicker").send_keys('02/01/2021')


#### case udah milih tanggal dan mau diganti ####
time.sleep(2)
driver.find_element(By.ID, "datepicker").clear()
time.sleep(2)
driver.find_element(By.ID, "datepicker").send_keys('05/08/2022')
