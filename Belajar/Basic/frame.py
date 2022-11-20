from selenium import webdriver
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")

driver.switch_to.frame("frame-left")
text1 = driver.find_element(By.XPATH, '/html/body').text
print(text1)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
text2 = driver.find_element(By.XPATH, '/html/body').text
print(text2)