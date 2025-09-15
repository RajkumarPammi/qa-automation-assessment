from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Update these after checking actual HTML
        self.CURRENT_PASSWORD = (By.ID, "oldPassword")
        self.NEW_PASSWORD = (By.ID, "newPassword")
        self.CONFIRM_PASSWORD = (By.ID, "confirmPassword")
        self.SAVE_BTN = (By.XPATH, "//button[contains(text(), 'Save')]")

    def change_password(self, current, new):
        self.wait.until(EC.visibility_of_element_located(self.CURRENT_PASSWORD)).send_keys(current)
        self.driver.find_element(*self.NEW_PASSWORD).send_keys(new)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(new)
        self.driver.find_element(*self.SAVE_BTN).click()
