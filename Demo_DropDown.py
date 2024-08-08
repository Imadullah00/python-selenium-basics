from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Demo_Dropdown():
    def Demo_Dropdown_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette')
        driver.maximize_window()
        dropdown = driver.find_element(By.TAG_NAME, "select")
        dd = Select(dropdown)
        dd.select_by_value("ATA")
        time.sleep(3)
        dd.select_by_index(3)
        time.sleep(3)
        dd.select_by_visible_text("Australia")
        time.sleep(3)


ddown = Demo_Dropdown()
ddown.Demo_Dropdown_m()

