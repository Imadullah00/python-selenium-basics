from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_FindElementbyID():
    def locate_by_id_demo(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.expedia.ca/')

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(3)


findbyid = Demo_FindElementbyID()
findbyid.locate_by_id_demo()


