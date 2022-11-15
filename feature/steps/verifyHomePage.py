from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()


@when('Open Inspire Home Page')
def OpenHomePage(context):
    context.driver.get("https://www.inspire.com/")


@then('Verify the Title of the Page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//img[@id='homeLogo']").is_displayed()
    assert status is True


@then('CLose The Browser')
def closeBrowser(context):
    context.driver.close()
