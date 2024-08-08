from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Demo_Sliders():

    def Demo_Sliders_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.globalsqa.com/demo-site/sliders/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
        time.sleep(2)
        achains = ActionChains(driver)
        achains.drag_and_drop_by_offset(driver.find_element(By.XPATH, "//div[@id='red']//span[@class='ui-slider-handle ui-corner-all ui-state-default']"), -100,0).perform()
        time.sleep(2)


DemoSdlr = Demo_Sliders()
DemoSdlr.Demo_Sliders_m()