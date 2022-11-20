from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://training.openspan.com/login")
demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
print(demo_state)
driver.find_element(By.ID, "user_name").send_keys("Testing")
driver.find_element(By.ID, "user_pass").send_keys("Testing")
demo_state2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
print(demo_state2)