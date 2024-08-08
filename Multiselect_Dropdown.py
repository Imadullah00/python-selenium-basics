from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Demo_MultiSelect_Dropdown():

    def Demo_MultiselectDropdown_m(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://demoqa.com/select-menu')
        driver.maximize_window()
        time.sleep(2)
        dd = driver.find_element(By.XPATH, "//select[@id='cars']")

        dd_multi = Select(dd)

        dd_multi.select_by_index(1)
        time.sleep(3)
        dd_multi.select_by_value("opel")
        time.sleep(3)
        dd_multi.select_by_visible_text("Audi")
        time.sleep(3)
        dd_multi.deselect_by_index(2)
        time.sleep(3)
        dd_multi.deselect_all()
        time.sleep(3)






ddown = Demo_MultiSelect_Dropdown()
ddown.Demo_MultiselectDropdown_m()

