from selenium.webdriver.common.by import By
from .base_page import BasePage

class AccountPage(BasePage):
    ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")  # for starting from home if needed
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")
    ACCOUNT_MENU = (By.LINK_TEXT, "Sign In")  # adapt as needed
    ACCOUNT_INFO = (By.LINK_TEXT, "Account Information")
    CURRENT_PASS = (By.ID, "current-password")
    NEW_PASS = (By.ID, "password")
    CONFIRM_PASS = (By.ID, "password-confirmation")
    SAVE_BUTTON = (By.XPATH, "//button[@title='Save']")

    def sign_out(self):
        self.click(self.SIGN_OUT)

    def go_to_account_info(self):
        self.click(self.ACCOUNT_INFO)

    def change_password(self, current, new):
        # open account info first
        self.type(self.CURRENT_PASS, current)
        self.type(self.NEW_PASS, new)
        self.type(self.CONFIRM_PASS, new)
        self.click(self.SAVE_BUTTON)
