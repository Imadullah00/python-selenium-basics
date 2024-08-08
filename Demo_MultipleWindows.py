from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_MultipleWindow():

    def Demo_MultipleWindow_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.browserstack.com/guide/handling-tabs-in-selenium")
        driver.maximize_window()
        parent = driver.current_window_handle
        print(parent)
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='Actions Class']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent:
                print(handle)
                driver.switch_to.window(handle)
                time.sleep(3)
                driver.find_element(By.XPATH, "//button[@id='accept-cookie-notification']").click()
                time.sleep(1)
                driver.find_element(By.XPATH, "//div[@class='social-share']//a[@title='Share on Facebook']").click()
                print("debug if")
                time.sleep(2)
                driver.close()

                break
        driver.switch_to.window(parent)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='accept-cookie-notification']").click()
        driver.find_element(By.XPATH, "//div[@class='social-share bottom-center']"
                                      "//a[@title='Share on Twitter']").click()
        time.sleep(3)


mp = Demo_MultipleWindow()
mp.Demo_MultipleWindow_m()
