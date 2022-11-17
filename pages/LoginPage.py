from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TXT_USERNAME = (By.ID, "email")
    TXT_PASSWORD = (By.ID, "pw")
    BTN_LOGIN = (By.ID, "login_submit")
    MSG_INVALIDCREDS = (By.ID, "login_error")
    JOIN_NOW_LINK = (By.XPATH, "//a[contains(.,'Join now!')]")
    REMEMBER_CHECKBOX = (By.ID, "remember")
    FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, "Forgot password")
    FB_AUTH = (By.ID, "fb-auth")
    GOOGLE_AUTH = (By.ID, "goog-auth")
    APPLE_AUTH = (By.ID, "apple-auth")

    """Constructor of Carrers Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.clear_element_text(self.TXT_USERNAME)
        self.input_element(self.TXT_USERNAME, user)
        self.clear_element_text(self.TXT_PASSWORD)
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_username(self, user):
        self.input_element(self.TXT_USERNAME, user)

    def enter_password(self, pwd):
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validateTitle(self):
        assert self.get_title() == "Inspire"

    def validateInvalidCreds(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Incorrect e-mail address or password. Please try again"

    # def validateEmptyUsername(self):
    #     assert self.get_element_text(self.MSG_INVALIDCREDS) == "Username cannot be empty"
    #
    # def validateEmptyPassword(self):
    #     assert self.get_element_text(self.MSG_INVALIDCREDS) == "Password cannot be empty"
