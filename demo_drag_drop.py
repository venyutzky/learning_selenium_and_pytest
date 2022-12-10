from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DemoDragDrop():

    def demo_drag_drop(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
        elem2 = driver.find_element(By.XPATH, "//div[@id='droppable']")
        achains = ActionChains(driver)
        achains.drag_and_drop_by_offset(elem1, 60, 50).perform()
        time.sleep(3)
        achains.drag_and_drop(elem1, elem2).perform()
        time.sleep(3)



ddragdrop = DemoDragDrop()
ddragdrop.demo_drag_drop()