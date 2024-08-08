from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_GetText():
    def demo_getText(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.google.com/')

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        time.sleep(3)

        attr_g = driver.find_element(By.XPATH, "//a[normalize-space()='Images']").get_attribute('aria-label')
        print(attr_g)


        #text = driver.find_element(By.XPATH, "//a[normalize-space()='Cancel your hotel or vacation rental booking']")
        #print(text.text)


findbyid = Demo_GetText()
findbyid.demo_getText()

