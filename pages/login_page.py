from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    email_input = (By.ID, "email")
    password_input = (By.ID, "password")

    login_btn_home = (By.XPATH, "//a[contains(text(),'Login')]")

    login_btn = (By.XPATH, "//button[@type='submit' and text()='Login']")

    logout_btn = (By.XPATH, "//button[contains(text(),'Logout')]")

    error_message = (
        By.XPATH,
        "//div[contains(text(),'Incorrect email address or password')]",
    )

    def __init__(self, driver):
        super().__init__(driver)
        

    # Open Login Page
    def go_to_login_page(self):
        self.click(self.login_btn_home)

    # Login
    def login(self, email, password):
        self.go_to_login_page()

        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)

        self.click(self.login_btn)

    # Verify Login
    def is_login_successful(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.logout_btn)
            ).is_displayed()

        except Exception:
            return False

    def is_error_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.error_message)
            ).is_displayed()

        except Exception:
            return False
