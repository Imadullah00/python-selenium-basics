from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager
s = Service(EdgeChromiumDriverManager().install())

#s = Service(ChromeDriverManager().install())

#s = Service("C:\\browserwebdriver\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
#driver = webdriver.Chrome(service=s)

driver = webdriver.Edge(service=s)

driver.get("https://www.espncricinfo.com/")
driver.maximize_window()
print(driver.title)

try:
 while(True):
    pass
except KeyboardInterrupt:
    pass