import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_DateHandle():

    def Demo_DateHandle_m(self):
        #s = Service(ChromeDriverManager().install())
        #driver = webdriver.Chrome(service=s)

        chrome_install = ChromeDriverManager().install()
        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        chrome_service = Service(chromedriver_path)

        driver = webdriver.Chrome(service=chrome_service)


        driver.get('https://www.yatra.com/')

        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        time.sleep(4)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == "07/08/2024":
                print("in if block")
                date.click()
                time.sleep(4)
                break




dt = Demo_DateHandle()
dt.Demo_DateHandle_m()
