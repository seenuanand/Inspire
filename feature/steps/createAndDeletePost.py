from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


@given(u'User Launches the Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


@when(u'User Opens the Home Page In Chrome and Clicks Sign In Button')
def VerifyHomepage(context):
    context.driver.get("https://www.inspire.com/")
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, "logIn")))
    context.driver.find_element(By.ID, "logIn").click()


@when(u'User Enters UserName "srinivas.anand1@gmail.com" And Password "Srinivas@12345" In Chrome')
def LoginWithCredentials(context, userName, password):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, "email")))
    context.driver.find_element(By.ID, "email").clear()
    context.driver.find_element(By.ID, "pw").clear()
    context.driver.find_element(By.ID, "email").send_keys(userName)
    context.driver.find_element(By.ID, "pw").send_keys(password)
    time.sleep(10)
    # Change to Explicit Wait Here wait for some element to be available


@when(u'User Clicks the Login Submit Button In Chrome')
def SubmitLogin(context):
    context.driver.find_element(By.ID, "login_submit").click()
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
    time.sleep(10)
    # Remove This used for Debugging


@when(u'User Must Successfully Login to His Dashboard Page In Chrome')
def VerifyDashboard(context):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
    verifyDashboard = context.driver.find_element(By.XPATH,
                                                  "//img[contains(@alt,'QA_candidate_SrinivasAnand')]").is_displayed()
    assert verifyDashboard is True


@when(u'User Selects Community Blood Pressure In Chrome')
def SelectCommunity(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Blood Pressure").click()
    time.sleep(10)
    # Remove this as it is used for debugging and put explicit wait if needed


@when(u'User Clicks Create Post Button In Chrome')
def CreateNewPost(context):
    elementNudge = context.driver.find_element(By.ID, "dismiss_nudge")
    if elementNudge:
        # elementNudge.click()
        context.driver.find_element(By.ID, "dismiss_nudge").click()
    context.driver.find_element(By.ID, "post_button").click()


@when(u'User Will Add All the mandatory Post Details and Submits Post In Chrome')
def AddPostDetails(context, postTitle="QA_Candiadte_" + str(random.randint(1, 1000)),
                   postDescription="QA_Candiadte_" + str(random.randint(1, 1000))):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(@id,'header_text')]")))
    value = context.driver.find_element(By.XPATH, "//h1[contains(@id,'header_text')]").text
    time.sleep(5)
    assert value == "Write a new post"
    print("The Title Value is :" + value)
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Choose Topic (required)')]")))
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//span[contains(.,'Choose Topic (required)')]").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//div[contains(@id,'item')][@class='pfsc-item'][contains(.,"
                                          "'Symptoms of high blood pressure')]").click()
    context.driver.find_element(By.ID, "post-title-textbox").click()
    context.driver.find_element(By.ID, "post-title-textbox").send_keys(postTitle)
    context.driver.find_element(By.XPATH, "//div[contains(@role,'textbox')]").click()
    context.driver.find_element(By.XPATH, "//div[contains(@role,'textbox')]").send_keys(postDescription)
    context.driver.find_element(By.XPATH, "//span[contains(.,'Public')]").click()
    context.driver.find_element(By.XPATH, "//div[contains(@id,'laebl')][@class='cdb-option cd-purple']["
                                          "contains(.,'Inspire Friends')]")
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//div[contains(@id,'laebl')][@class='cdb-option cd-purple']["
                                          "contains(.,'Inspire Friends')]").click()
    context.driver.find_element(By.ID, "submit-post-button").click()

    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(.,'" + postDescription + "')]")))

    value1 = context.driver.find_element(By.XPATH, "//p[contains(.,'" + postDescription + "')]").text
    assert value1 == postDescription
    print("The New Post Title is :" + value1)

    print("Post Submitted successfully")
    time.sleep(5)


@when('New Post is Successfully Created Verified')
def VerifyPostTitleAndSelect(context):
    print("Work In Progress")


@then(u'Delete the Newly Created Post and Logout')
def DeleteThePostAndDelete(context):
    print("Work In Progress")
