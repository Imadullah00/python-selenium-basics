from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_JSPopupAlert():

    def Demo_JSPopupalert_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)

        #click ok
        driver.switch_to.alert.accept()
        time.sleep(2)
        #click dismiss
        #driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        #send keys
        #driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Imadullah")
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(3)


popup = Demo_JSPopupAlert()
popup.Demo_JSPopupalert_m()

