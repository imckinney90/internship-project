from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.offplan_page import OffPlanPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.offplan_page = OffPlanPage(driver)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url