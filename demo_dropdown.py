from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoDropdown():
    
    def demo_dropdown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.salesforce.com/ap/form/signup/freetrial-sales/?d=topnav2-btn-ft")


checkbox = DemoDropdown()
# checkbox.demo_checkbox()
checkbox.demo_dropdown()