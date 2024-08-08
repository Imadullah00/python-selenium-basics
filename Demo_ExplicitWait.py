from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Demo_ExplicitWait():

    def Demo_ExplicitWait_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.google.ca/')
        wait = WebDriverWait(driver,10, 5, ignored_exceptions=[ElementClickInterceptedException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='APjFqb']"))).click()
        #driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").click()
        #time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("New")
        time.sleep(2)

        test = driver.find_elements(By.XPATH, "//div[@class='erkvQe']//div[1]/ul/li")
        time.sleep(2)
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



autosug = Demo_ExplicitWait()
autosug.Demo_ExplicitWait_m()

