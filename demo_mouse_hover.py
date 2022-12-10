from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DemoMouseHover():

    def demo_mouse_hover(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        myaccount = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")

        achains = ActionChains(driver)
        achains.move_to_element(myaccount).perform()
        time.sleep(2)
        achains.move_to_element(morebutton).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(2)

demomousehover = DemoMouseHover()
demomousehover.demo_mouse_hover()