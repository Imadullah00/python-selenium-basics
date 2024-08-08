from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_DrangnDrop():

    def Demo_Sliders_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        time.sleep(2)
        achains = ActionChains(driver)
        achains.drag_and_drop_by_offset(driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']"), 170, 30).perform()
        time.sleep(2)

ddrop = Demo_DrangnDrop()
ddrop.Demo_Sliders_m()

