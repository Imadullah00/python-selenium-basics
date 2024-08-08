from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_Element_State():
    def Demo_Enable_Disable(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =s)
        driver.get('https://training.openspan.com/login')
        state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("admin")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("temp_pwd")
        time.sleep(1)
        state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state)


findbyid = Demo_Element_State()
findbyid.Demo_Enable_Disable()
