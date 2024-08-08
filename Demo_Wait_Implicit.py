from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Demo_ImplicitWait():

    def Demo_ImplicitWait_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.implicitly_wait(10)
        driver.get('https://login.salesforce.com/')
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("admin123")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("temppwd")

        time.sleep(1)


ImpWait = Demo_ImplicitWait()
ImpWait.Demo_ImplicitWait_m()
