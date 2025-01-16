from pages.base_page import BasePage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)