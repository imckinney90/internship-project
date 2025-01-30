from time import sleep
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN = (By.CSS_SELECTOR, "[wized='loginButton']")
    MOBILE_LOGIN = (By.CSS_SELECTOR, ".login-button.w-button")
    PAGE_BODY = (By.TAG_NAME, 'body')

    def login(self, email="imckinney1@hotmail.com", password="Newport#90"):
        self.input_text(email, self.EMAIL)
        self.input_text(password, self.PASSWORD)
        self.click(self.LOGIN)

    def login_mobile_web(self, email="imckinney1@hotmail.com", password="Newport#90"):
        # Input credentials
        self.input_text(email, self.EMAIL)
        self.input_text(password, self.PASSWORD)
        sleep(8)
        self.click_page_body(*self.PAGE_BODY)
        self.click(self.MOBILE_LOGIN)
