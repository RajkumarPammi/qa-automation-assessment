from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMAIL = (By.XPATH, "//input[@placeholder='Email']")
    COUNTRY = (By.XPATH, "//input[@placeholder='Country of Nationality']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@placeholder='Confirm Password']")
    REGISTER_BTN = (By.XPATH, "//button[normalize-space()='Register']")

    def fill_signup_form(self, first, last, email, country, password):
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)

    def click_register(self):
        self.driver.find_element(*self.REGISTER_BTN).click()
