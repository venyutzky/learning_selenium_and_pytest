from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class DemoImplicitWait():
    
    def demo_implicit_wait(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=au")
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Belajar Selenium")
        driver.find_element(By.XPATH, "//input[@id='password']3").send_keys("asbassd")

impwait = DemoImplicitWait()
impwait.demo_implicit_wait()
