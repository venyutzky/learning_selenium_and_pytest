from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DemoRighClickDoubleClick():

    def demo_righClick_doubleClick(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        # Double click
        achains = ActionChains(driver)
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(elem2).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

        # Right Click
        # achains = ActionChains(driver)
        elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        achains.context_click(elem1).perform()
        time.sleep(3)
        copyelem.click()
        time.sleep(2)
        driver.switch_to.alert.accept()

     


drightclick = DemoRighClickDoubleClick()
drightclick.demo_righClick_doubleClick()

