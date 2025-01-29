from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def login(self, email="imckinney1@hotmail.com", password="Newport#90"):
        self.input_text(email, self.EMAIL)
        self.input_text(password, self.PASSWORD)
        self.click(self.LOGIN)

