from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_MouseHover():

    def Demo_MouseHover_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        achains = ActionChains(driver)
        achains.move_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")).perform()
        time.sleep(2)
        achains.move_to_element(driver.find_element(By.XPATH, "//span[@class='more-arr']")).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Adventures']").click()
        time.sleep(4)



mhover = Demo_MouseHover()
mhover.Demo_MouseHover_m()


