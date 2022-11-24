from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoRadio():
    
    def demo_radio_button(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.find_element(By.ID, "sex-0").click()
        time.sleep(1)
        driver.find_element(By.ID, "exp-2").click()
        time.sleep(1)
        driver.find_element(By.ID, "exp-0").click()
        print(driver.find_element(By.ID, "exp-0").is_selected())
        print(driver.find_element(By.ID, "exp-2").is_selected())
        time.sleep(1)


checkbox = DemoRadio()
# checkbox.demo_checkbox()
checkbox.demo_radio_button()