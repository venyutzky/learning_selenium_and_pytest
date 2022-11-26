from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoMultipleWindows():
    
    def demo_windows(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Yatra Kenya Tourism']//img[@class='conta iner large-banner']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                # driver.find_element(By.XPATH, "//body/form[@id='aspnetForm']/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxUpdatePanel']/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxDropZone']/div[contains(@data-ux-pagebuilder,'Column')]/ul/li/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxColumnDisplay_ctl00_uxControlColumn_ctl00_uxWidgetHost_uxUpdatePanel']/div[contains(@data-ux-pagebuilder,'Widget')]/div[contains(@class,'widgetBody')]/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxColumnDisplay_ctl00_uxControlColumn_ctl00_uxWidgetHost_uxWidgetHost_widget_CB']/div[contains(@class,'content-wrapper')]/div[contains(@class,'wrapper')]/div[contains(@class,'article-content editor')]/ul[contains(@class,'')]/li[1]/a[1]/span[1]/span[1]").click()
                articles_list = driver.find_elements(By.XPATH, "//body/form[@id='aspnetForm']/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxUpdatePanel']/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxDropZone']/div[contains(@data-ux-pagebuilder,'Column')]/ul/li/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxColumnDisplay_ctl00_uxControlColumn_ctl00_uxWidgetHost_uxUpdatePanel']/div[contains(@data-ux-pagebuilder,'Widget')]/div[contains(@class,'widgetBody')]/div[@id='ctl00_ContentPlaceHolderBody_ContentDropZone_uxColumnDisplay_ctl00_uxControlColumn_ctl00_uxWidgetHost_uxWidgetHost_widget_CB']/div[contains(@class,'content-wrapper')]/div[contains(@class,'wrapper')]/div[contains(@class,'article-content editor')]//ul//li//a")
                for article in articles_list:
                    if article.get_attribute("href") == "https://www.thomascook.in/holidays/international-tour-packages/kenya-tour-packages":
                        article.click()
                        time.sleep(3)
                        break
                time.sleep(3)
                driver.close()  
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title='Yatra ICICI Winter Carnival Offer']//img[@class='conta iner large-banner']").click()

        
    

    
dmultiplewindows = DemoMultipleWindows()
dmultiplewindows.demo_windows()

