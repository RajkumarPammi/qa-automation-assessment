from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.EMAIL_FIELD = (By.NAME, "email")
        self.PASSWORD_FIELD = (By.NAME, "password")
        self.SIGN_IN_BTN = (By.ID, "kt_login_signin_submit")
        self.SIGN_UP_LINK = (By.LINK_TEXT, "Sign Up")  # adjust if different

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        # Button becomes clickable only after valid input
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BTN)).click()

    def click_sign_up(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_LINK)).click()
