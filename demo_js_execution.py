from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoJS():
    
    def demo_javascript(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        # driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(10)
        demo_element = driver.execute_script("return document.getElementsByTagName('a')[8];")
        driver.execute_script("arguments[0].click();", demo_element)

demojs = DemoJS()
demojs.demo_javascript()