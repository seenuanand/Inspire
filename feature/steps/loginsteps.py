# from behave import *
# from selenium import webdriver
# from configuration.config import TestData
# from pages.LoginPage import LoginPage
# from pages.HomePage import HomePage
#
#
# @given('Launch the browser')
# def launch_browser(context):
#     if TestData.BROWSER == 'chrome':
#         context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     elif TestData.BROWSER == 'firefox':
#         context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
#     else:
#         raise ValueError('Browser is not supported')
#
#
# @when('Open the https://www.inspire.com/ website')
# def open_login_page(context):
#     try:
#         context.driver.get(TestData.URL)
#         context.loginPage = LoginPage(context.driver)
#         context.homepage = HomePage(context.driver)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in open login page section"
#
#
# @then('The login portal has been opened')
# def validate_login_page(context):
#     try:
#         context.loginPage.validateTitle()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validate login page title"
#
#
# @then('Provide the username "{user}" and password "{pwd}"')
# def enter_login_creds(context, user, pwd):
#     try:
#         context.loginPage.enter_login_credentials(user, pwd)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter login credentials"
#
#
# @then('Click on the Login button')
# def enter_login(context):
#     try:
#         context.loginPage.enter_login()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter login"
#
#
# @then('Login is successful and dashboard is opened')
# def validate_dashboard_page(context):
#     try:
#         context.dashboardpage.validatePageLoaded()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validating dashboard"
#
#
# @then(u'Login is failed and invlid credential error is displayed')
# def validate_invalid_login(context):
#     try:
#         context.loginPage.validateInvalidCreds()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validating invalid login"
#
#
# @then('Provide the password "{pwd}"')
# def enter_login_creds(context, pwd):
#     try:
#         context.loginPage.enter_password(pwd)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter password"
#
#
# @then('Provide the username "{user}"')
# def enter_login_creds(context, user):
#     try:
#         context.loginPage.enter_username(user)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter username"
#
#
# @then('Login is failed and empty username error is displayed')
# def validate_empty_username(context):
#     try:
#         context.loginPage.validateEmptyUsername()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validate empty username"
#
#
# @then('Login is failed and empty password error is displayed')
# def validate_empty_passeword(context):
#     try:
#         context.loginPage.validateEmptyPassword()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validate empty password"
#
#
# @then('Close the browser')
# def step_impl(context):
#     context.driver.close()
