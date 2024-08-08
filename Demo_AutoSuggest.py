from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Demo_AutoSuggest_Dropdown():

    def Demo_AutoSuggestDropdown_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.google.ca/')
        driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").click()
        driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("New")
        time.sleep(2)
        test = driver.find_elements(By.XPATH, "//div[@class='erkvQe']//div[1]/ul/li")
        print(len(test))

        for options in test:
            if "new york times" in options.text:
                options.click()
                break

        time.sleep(2)



        #driver.find_element(By.XPATH, "//span[normalize-space()='New York Rangers']").click()
        #time.sleep(3)


        #driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").click()
        #driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("New")
        #time.sleep(2)
        #driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys(Keys.ENTER)
        #time.sleep(3)



autosug = Demo_AutoSuggest_Dropdown()
autosug.Demo_AutoSuggestDropdown_m()

