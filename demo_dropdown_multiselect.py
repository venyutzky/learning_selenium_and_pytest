from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoDropdownMultiSelect():
    
    def demo_dropdown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        dd_demo = driver.find_element(By.ID, "multi-select")
        dd_multi = Select(dd_demo)

        dd_multi.select_by_value("California")
        time.sleep(1)
        dd_multi.select_by_visible_text("Pennsylvania")
        time.sleep(1)
        dd_multi.select_by_index(2)
        time.sleep(1)
        dd_multi.deselect_by_visible_text("California")
        time.sleep(1)
        dd_multi.select_by_value("New York")

dropdown = DemoDropdownMultiSelect()
# checkbox.demo_checkbox()
dropdown.demo_dropdown()