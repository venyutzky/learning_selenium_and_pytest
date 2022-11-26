from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoScreenshot():
    
    def demo_screen_capture(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        
        continueBtn = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        time.sleep(2)
        continueBtn.screenshot(".\\screenshot_demo_screen_capture.png")

        continueBtn.click()
        time.sleep(2)
        driver.get_screenshot_as_file(".\\error.png")
        driver.save_screenshot(".\\Belajar\\error.png")

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_capture()