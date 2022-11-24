from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoCheckBoxes():

    def demo_checkbox(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']").click()
        
        time.sleep(2)
        var1 =  driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']").is_selected()
        print(var1)

checkbox = DemoCheckBoxes()
# checkbox.demo_checkbox()
checkbox.demo_checkbox()