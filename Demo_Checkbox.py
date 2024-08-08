from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_Checkbox():
    def Demo_Checkbox_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s) 
        driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
        sel = driver.find_element(By.XPATH, "//input[@id='isAgeSelected']").is_selected()
        print(sel)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='isAgeSelected']").click()
        time.sleep(2)
        sel = driver.find_element(By.XPATH, "//input[@id='isAgeSelected']").is_selected()
        print(sel)


check = Demo_Checkbox()
check.Demo_Checkbox_m()
