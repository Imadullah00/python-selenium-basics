from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_RadioButton():
    def Demo_RadioBtn_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://practice.expandtesting.com/radio-buttons')
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='football']").click()
        time.sleep(3)


check = Demo_RadioButton()
check.Demo_RadioBtn_m()