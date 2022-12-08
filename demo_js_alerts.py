from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoJSPopup():

    def demo_js_alerts(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")

        #Accept alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

        #Dismiss alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        #Send keys alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Spongebob")
        driver.switch_to.alert.accept()
        time.sleep(2)

demopopup = DemoJSPopup()
demopopup.demo_js_alerts()

