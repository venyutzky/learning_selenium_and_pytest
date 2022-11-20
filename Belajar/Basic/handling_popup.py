from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

for i in range(2):
    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div")))
        print("Pop up muncul")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/modal-dialog/div/div/form/div/div/a").click()
        print("pop up diclose")

    except TimeoutException:
        print("Pop up tidak muncul")
        pass

    time.sleep(3)
