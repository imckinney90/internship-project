from .base_page import BasePage


class MainPage(BasePage):
    BASE_URL = 'https://soft.reelly.io/'

    def open_main(self):
        self.open_url(self.BASE_URL)