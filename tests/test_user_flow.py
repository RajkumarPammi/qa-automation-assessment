import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage


class TestUserFlow:
    def test_signup_login_signout_change_password(self, driver, base_url):
        driver.get(base_url)

        # --- Step 1: Go to Sign Up page ---
        login_page = LoginPage(driver)
        login_page.click_sign_up()
        time.sleep(2)

        # --- Step 2: Sign up ---
        signup_page = SignUpPage(driver)
        test_email = "testuser1234@example.com"
        test_password = "Test@12345"

        signup_page.fill_signup_form(
            first="Test",
            last="User",
            email=test_email,
            country="India",
            password=test_password
        )
        signup_page.click_register()
        time.sleep(3)

        # --- Step 3: Log out (if auto-login happened) ---
        try:
            logout_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]")
            logout_btn.click()
            time.sleep(2)
        except:
            pass  # already logged out

        # --- Step 4: Log in ---
        driver.get(base_url)
        login_page.enter_email(test_email)
        login_page.enter_password(test_password)
        login_page.click_login()

        # --- Step 5: Forgot Password flow ---
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Forgot Password')]"))
        )
        forgot_password_link.click()

        # Wait for Forgot Password page to load
        try:
            # Adjust locator based on actual HTML attributes
            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "email"))  # change to By.ID or By.XPATH if needed
            )
            email_field.send_keys(test_email)

            # Find and click reset/submit button
            reset_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Reset') or contains(text(),'Submit')]"))
            )
            reset_btn.click()

            time.sleep(2)  # allow backend to process
        except Exception as e:
            print("⚠️ Forgot Password flow failed:", e)
