from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_HiddenElement():
    def Demo_Display_Hide(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        disp = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(disp)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)
        disp = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(disp)

findbyid = Demo_HiddenElement()
findbyid.Demo_Display_Hide()
