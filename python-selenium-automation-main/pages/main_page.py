from .base_page import BasePage
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    BASE_URL = 'https://soft.reelly.io/'

    def open_main(self):
        try:
            self.open_url(self.BASE_URL)
        except Exception as e:
            raise Exception(f"Failed to open main page: {str(e)}")