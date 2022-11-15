from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

browser_Type = "Chrome"
browser = True

if browser_Type == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    browser = True
elif browser_Type == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser = True
else:
    print("No Browser is selected")
    browser = False

if browser:
    driver.get("https://inspire.com")
    driver.maximize_window()
    time.sleep(2)
    driver.close()
    driver.quit()
