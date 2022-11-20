from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver =  webdriver.Chrome()

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
driver.implicitly_wait(10)

dragable = driver.find_element(By.ID, "draggable")
dropable = driver.find_element(By.ID, "droppable")

action = ActionChains(driver)

action.drag_and_drop(dragable, dropable).perform()