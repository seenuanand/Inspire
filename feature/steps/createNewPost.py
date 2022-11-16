from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from configuration.config import TestData
from pages.HomePage import HomePage

@given('User Launches Chrome Browser')
def Launch_Browser(context):
    # Driver Option Selected From Configuration File
    if TestData.BROWSER == 'chrome':
        context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    elif TestData.BROWSER == 'firefox':
        context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    else:
        raise ValueError('Browser is not supported')

    # Can be Used when the Driver is copied to environment Script folder
    # if TestData.BROWSER == 'chrome':
    #     context.driver = webdriver.Chrome()
    # elif TestData.BROWSER == 'firefox':
    #     context.driver = webdriver.Firefox()
    # else:
    #     raise ValueError('Browser is not supported')

    # Driver Option To Install latest Driver from Web Driver Manager
    # if TestData.BROWSER == 'chrome':
    #     context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # elif TestData.BROWSER == 'firefox':
    #     context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # else:
    #     raise ValueError('Browser is not supported')

    context.driver.delete_all_cookies()
    context.driver.maximize_window()


@when('User Clicks the Login Button in the Home Page')
def VerifyHomepage(context):
    try:
        context.driver.get(TestData.URL)
        context.homepage = HomePage(context.driver)
        context.driver.find_element(By.ID, "logIn").click()
    except:
        context.driver.close()
        assert False, "Test is failed in Loading the Home Page"

@when('User Enters Valid User Name "{userName}" and Password "{password}"')
def LoginWithCredentials(context, userName, password):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, "email")))
    context.driver.find_element(By.ID, "email").clear()
    context.driver.find_element(By.ID, "pw").clear()
    context.driver.find_element(By.ID, "email").send_keys(userName)
    context.driver.find_element(By.ID, "pw").send_keys(password)
    time.sleep(10)
    # Change to Explicit Wait Here wait for some element to be available


@when('User Click the Login Button')
def SubmitLogin(context):
    context.driver.find_element(By.ID, "login_submit").click()
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
    time.sleep(10)
    # Remove This used for Debugging


@when('User Must Successfully Login to His Dashboard Page')
def VerifyDashboard(context):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
    verifyDashboard = context.driver.find_element(By.XPATH,
                                                  "//img[contains(@alt,'QA_candidate_SrinivasAnand')]").is_displayed()
    assert verifyDashboard is True


@when('User Selects Community Blood Pressure')
def SelectCommunity(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Blood Pressure").click()
    time.sleep(10)
    # Remove this as it is used for debugging and put explicit wait if needed


@when('User Clicks Create Post Button')
def CreateNewPost(context):
    elementNudge = context.driver.find_element(By.ID, "dismiss_nudge")
    if elementNudge:
        # elementNudge.click()
        context.driver.find_element(By.ID, "dismiss_nudge").click()
    context.driver.find_element(By.ID, "post_button").click()


@when('User Will add all the mandatory Post Details and Submits Post')
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


@then('New Post is Successfully Created Verified and logout of the application')
def LogoutAndCloseBrowser(context):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[@id='profile-menu-icon']")))
    context.driver.find_element(By.XPATH, "//a[@id='profile-menu-icon']").click()
    context.driver.find_element(By.XPATH, "//a[@id='logOut']").click()
    context.driver.close()
