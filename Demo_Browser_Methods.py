from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Demo_SeleniumLearning():
    def demo_browser_methods(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.google.ca/')
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

        print(driver.current_url)
        print(driver.title)
        driver.find_element(By.LINK_TEXT, 'About').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.forward()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        driver.fullscreen_window()
        time.sleep(1)
        driver.minimize_window()
        time.sleep(2)
        driver.quit()


findbyid = Demo_SeleniumLearning()
findbyid.demo_browser_methods()
