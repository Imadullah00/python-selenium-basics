from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_MultipleFrames():

    def Demo_MultipleFrames_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='W3Schools HTML Tutorial']"))
        driver.find_element(By.XPATH, "//a[normalize-space()='Study our free HTML Tutorial »']").click()
        time.sleep(1.5)


mframes = Demo_MultipleFrames()
mframes.Demo_MultipleFrames_m()
