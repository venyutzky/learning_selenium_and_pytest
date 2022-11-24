from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoDropdown():
    
    def demo_dropdown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.salesforce.com/ap/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdwn = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdwn)
        dd.select_by_index(1)
        time.sleep(1)
        dd.select_by_visible_text("IT Manager")
        time.sleep(1)
        dd.select_by_value("Others_AP")


dropdown = DemoDropdown()
# checkbox.demo_checkbox()
dropdown.demo_dropdown()