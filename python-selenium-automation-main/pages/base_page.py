from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find_element(self, locator, timeout=10):
        try:
            wait = self.long_wait if timeout == 20 else self.wait
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not found after {timeout} seconds")

    def find_elements(self, locator, timeout=10):
        try:
            wait = self.long_wait if timeout == 20 else self.wait
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            if not elements:
                raise ElementNotVisibleException(f"No elements found for {locator}")
            return elements
        except TimeoutException:
            raise TimeoutException(f"Elements {locator} not found after {timeout} seconds")

    def input_text(self, text, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise TimeoutException(f"Input field {locator} not found after 10 seconds")

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            sleep(1)
        except Exception as e:
            raise Exception(f"Failed to scroll to element: {str(e)}")

    def scroll_page_to_bottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        self.driver.execute_script("window.scrollTo(0, 0);")


