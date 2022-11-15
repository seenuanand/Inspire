from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User Launches the Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


@when('User Opens the Home Page and Clicks Sign In Button')
def VerifyHomepage(context):
    context.driver.get("https://www.inspire.com/")
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, "logIn")))
    context.driver.find_element(By.ID, "logIn").click()


@when('User Enters UserName "{userName}" And Password "{password}"')
def LoginWithCredentials(context, userName, password):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, "email")))
    context.driver.find_element(By.ID, "email").clear()
    context.driver.find_element(By.ID, "pw").clear()
    context.driver.find_element(By.ID, "email").send_keys(userName)
    context.driver.find_element(By.ID, "pw").send_keys(password)
    time.sleep(10)
    # Change to Explicit Wait Here wait for some element to be available


@when('User Clicks the Login Submit Button')
def SubmitLogin(context):
    context.driver.find_element(By.ID, "login_submit").click()
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
    time.sleep(10)
    # Remove This used for Debugging


@then('User Must Successfully Login to His Dashboard Page')
def VerifySuccessfulLogin(context):

    context.driver.find_element(By.XPATH, "//a[@id='profile-menu-icon']").click()
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Sign out')]")))
    context.driver.find_element(By.XPATH, "//a[contains(.,'Sign out')]").click()
    time.sleep(5)
    # Change to Explicit Wait Here wait for some element to be available
    context.driver.close()
