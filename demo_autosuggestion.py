from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class DemoAutoSuggest():
    
    def demo_autosuggest_dropdown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)
        going_to =  driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")
        time.sleep(2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

dauto = DemoAutoSuggest()
dauto.demo_autosuggest_dropdown()