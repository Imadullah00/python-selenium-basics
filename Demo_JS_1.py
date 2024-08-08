from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_JS():

    def Demo_JS_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.execute_script("window.open('https://www.facebook.com/login.php/' , '_self');")
        driver.maximize_window()
        #driver.get('https://www.facebook.com/login.php/')
        btn = driver.execute_script("return document.getElementsByTagName('button')[0];")
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(5)


js = Demo_JS()
js.Demo_JS_m()
