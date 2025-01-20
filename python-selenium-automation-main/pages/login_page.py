from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def enter_email(self, email):
        self.input_text(email, self.EMAIL)

    def enter_password(self, password):
        self.input_text(password, self.PASSWORD)

    def click_continue_button(self):
        self.click(self.LOGIN)

    def login(self, email="reelly_careerist_test@proton.me", password="Test"):
        self.enter_email(email)
        self.enter_password(password)
        self.click_continue_button()


