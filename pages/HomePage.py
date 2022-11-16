from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SIGNIN_BTN = (By.ID, "logIn")
    SIGNUP_BTN = (By.ID, "signUp")
    SEARCH_TXT = (By.ID, "search_textbox")
    DISCOVER_MENU = (By.ID, "toggle_discover_menu")
    COMMUNITY_MENU = (By.ID, "toggle_community_menu")
    FIND_SUPPORT_TXT = (By.ID, "searchBlock")
    SEARCH_OUR_COMMUNITY_BTN = (By.XPATH, "//button[contains(.,'Search Our Communities')]")
    LEARN_MORE_ANCHOR = (By.XPATH, "//a[@target='_blank'][contains(.,'Learn more')]")
    BECOME_PARTNER_BTN = (By.XPATH, "//button[contains(.,'Become a Partner')]")

    def __init__(self, driver):
        super().__init__(driver)

    def validatePageLoaded(self):
        self.verify_element_displayed(self.COMMUNITY_MENU)
        assert self.get_element_text(self.COMMUNITY_MENU) == "Communities"

    def validateElementEnabled_Disabled(self):
        elementState = self.verify_element_enabled(self.SIGNIN_BTN)
        return elementState

    def click_Login_Button(self):
        self.click_element(self.SIGNIN_BTN)
