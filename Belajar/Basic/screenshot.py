from selenium import webdriver
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless =  True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https:/demoqa.com")
print(driver.title)
driver.get_screenshot_as_file("screenshot2.png")
