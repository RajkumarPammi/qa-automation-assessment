from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    # Locator for the logout button
    # You will need to inspect the dashboard page to find the correct locator for the logout button
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout')]")

    def click_logout(self):
        """Clicks the logout button on the dashboard page."""
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()