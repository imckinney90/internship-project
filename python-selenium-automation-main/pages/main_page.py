from .base_page import BasePage

class MainPage(BasePage):
    def open_main(self):
        self.open_url('https://soft.reelly.io/')