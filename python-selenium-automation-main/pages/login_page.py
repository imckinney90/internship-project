from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def enter_email(self, email):
        try:
            self.input_text(email, self.EMAIL)
        except TimeoutException:
            raise TimeoutException("Email field not accessible")

    def enter_password(self, password):
        try:
            self.input_text(password, self.PASSWORD)
        except TimeoutException:
            raise TimeoutException("Password field not accessible")

    def click_continue_button(self):
        try:
            self.click(self.LOGIN)
        except TimeoutException:
            raise TimeoutException("Login button not clickable")

    def login(self, email="imckinney1@hotmail.com", password="Newport#90"):
        try:
            self.enter_email(email)
            self.enter_password(password)
            self.click_continue_button()
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")


