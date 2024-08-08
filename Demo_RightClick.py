from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_RightClick():

    def Demo_RightClick_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        achains = ActionChains(driver)
        achains.context_click(driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()

        achains.double_click(driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")).perform()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(2)


rightclk = Demo_RightClick()
rightclk.Demo_RightClick_m()