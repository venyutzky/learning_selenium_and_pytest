from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoIframe ():
    
    def demo_frames(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.switch_to.frame("iframeResult")
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='w3loginbtn']").click()
        time.sleep(2)


diframe = DemoIframe()
diframe.demo_frames()


