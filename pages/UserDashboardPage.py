from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from configuration.config import TestData

USER_NAME = (By.XPATH, "//img[contains(@alt,'"+TestData.USERNAME+"')]")

class UserDashboardPage(BasePage):


    """Constructor of Carrers Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_community_link(self, PARTIAL_LINK):
        self.click_element((By.PARTIAL_LINK_TEXT, self.PARTIAL_LINK))

    def verify_User_Name(self):
        self.verify_element_displayed((By.XPATH, USER_NAME))

