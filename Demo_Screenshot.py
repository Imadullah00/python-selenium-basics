from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_Screenshot():

    def Demo_Screenshot_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get('https://www.facebook.com/login.php/')
        driver.maximize_window()
        lgn = driver.find_element(By.XPATH, "//button[@id='loginbutton']")
        lgn.screenshot(".\\test.png")
        lgn.click()
        time.sleep(2)
        driver.save_screenshot(".\\test2.png")
        driver.get_screenshot_as_file("C:\\PythonSelenium\\test3.png")


ss = Demo_Screenshot()
ss.Demo_Screenshot_m()
