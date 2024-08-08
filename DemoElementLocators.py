from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager

class Demo_FindElementbyID():
    def locate_by_id_demo(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.expedia.ca/')
        driver.find_element(By.PARTIAL_LINK_TEXT, 'List your proper').click()
        #driver.find_element(By.ID, 'loginFormEmailInput').send_keys('test@test.com')
        driver.find_element(By.XPATH, "//img[@alt='Lodging']").click()
        #driver.find_element(By.CSS_SELECTOR, '#loginFormEmailInput').send_keys('test@test.com')
        time.sleep(5)


findbyid = Demo_FindElementbyID()
findbyid.locate_by_id_demo()




