# Generated by Selenium IDE
from _ast import Assert

import pytest
import time
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestInspireTestScript():

    # def get_clear_browsing_button(driver):
    #     """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    #     return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
    #
    # def clear_cache(driver, timeout=60):
    #     """Clear the cookies and cache for the ChromeDriver instance."""
    #     # navigate to the settings page
    #     driver.get('chrome://settings/clearBrowserData')
    #
    #     # wait for the button to appear
    #     wait = WebDriverWait(driver, timeout)
    #     wait.until(self.get_clear_browsing_button)
    #
    #     # click the button to clear the cache
    #     driver.get_clear_browsing_button(driver).click()
    #
    #     # wait for the button to be gone before returning
    #     wait.until_not(driver.get_clear_browsing_button)

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_postamessage(self, postTitle="QA Post 1", postDescription="QA Post 1"):
        self.driver.get("https://www.inspire.com/")
        # Check For Good Resolution based on the Application Support documents
        # self.driver.set_window_size(1382, 744)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "logIn")))

        self.driver.find_element(By.ID, "logIn").click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "email")))
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "pw").clear()
        self.driver.find_element(By.ID, "email").send_keys("srinivas.anand1@gmail.com")
        self.driver.find_element(By.ID, "pw").send_keys("Srinivas@12345")
        self.driver.find_element(By.ID, "login_submit").click()
        time.sleep(10)
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Blood Pressure")))
            print("Post Login Page is ready!")
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Blood Pressure").click()
            time.sleep(10)
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "post_button")))
                print("Community Page Loaded")
                elementNudge = self.driver.find_element(By.ID, "dismiss_nudge")
                if elementNudge:
                    elementNudge.click()
                self.driver.find_element(By.ID, "post_button").click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[contains(@id,'header_text')]")))
                value = self.driver.find_element(By.XPATH, "//h1[contains(@id,'header_text')]").text
                time.sleep(5)
                assert value == "Write a new post"
                print("The Title Value is :" + value)
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Choose Topic (required)')]")))
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//span[contains(.,'Choose Topic (required)')]").click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//div[contains(@id,'item')][@class='pfsc-item'][contains(.,"
                                                   "'Symptoms of high blood pressure')]").click()
                self.driver.find_element(By.ID, "post-title-textbox").click()
                self.driver.find_element(By.ID, "post-title-textbox").send_keys(postTitle)
                self.driver.find_element(By.XPATH, "//div[contains(@role,'textbox')]").click()
                self.driver.find_element(By.XPATH, "//div[contains(@role,'textbox')]").send_keys(postDescription)
                self.driver.find_element(By.XPATH, "//span[contains(.,'Public')]").click()
                self.driver.find_element(By.XPATH, "//div[contains(@id,'laebl')][@class='cdb-option cd-purple']["
                                                   "contains(.,'Inspire Friends')]")
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//div[contains(@id,'laebl')][@class='cdb-option cd-purple']["
                                                   "contains(.,'Inspire Friends')]").click()
                self.driver.find_element(By.ID, "submit-post-button").click()

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//p[contains(.,'" + postDescription + "')]")))

                value1 = self.driver.find_element(By.XPATH, "//p[contains(.,'" + postDescription + "')]").text
                assert value1 == postDescription
                print("The New Post Title is :"+value1)

                print("Post Submitted successfully")

                time.sleep(5)
                self.driver.find_element(By.XPATH, "//a[@id='profile-menu-icon']").click()
                self.driver.find_element(By.XPATH, "//a[@id='logOut']").click()
                self.driver.close()
            except TimeoutException:
                print("Loading took too much time to Load to Community Page!")
                self.driver.close()
        except TimeoutException:
            print("Loading took too much time to Load to Dashboard!")
            self.driver.close()
