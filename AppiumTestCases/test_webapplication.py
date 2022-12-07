import time

from appium import webdriver
from configuration.config import TestData

android_desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)
IOS_desired_caps = dict(
    deviceName='IOS',
    platformName='IOS',
    browserName='Chrome'
)

Device = None
if TestData.PLATFORM == 'Android':
    Device = 'Android'
elif TestData.PLATFORM == 'IOS':
    Device = 'IOS'
else:
    print("Device not Available")

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Device)
driver.get("https://www.inspire.com/")
print(driver.title)
time.sleep(5)
driver.quit()
