from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoHiddenElements():

    def demo_is_displayed(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

    def demo_is_displayed_yatra(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]").click()
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[1]').click()
        time.sleep(2)
        elem1 = driver.find_elements(By.XPATH,"//select[@class='ageselect']") 
        if len(elem1) == 0:
            print("Element is not in DOM")
        if len(elem1) > 0 and elem1[0].is_displayed()==False:
            print("Element is in DOM but not displayed")
        # print(elem1)

demoDisplayed = DemoHiddenElements()
# demoDisplayed.demo_is_displayed()
demoDisplayed.demo_is_displayed_yatra()