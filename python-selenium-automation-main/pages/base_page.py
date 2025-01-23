from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.long_wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    def open_url(self, url):
        try:
            self.driver.get(url)

            self.wait.until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )

            sleep(2)
        except Exception as e:
            print(f"Failed to load URL {url}: {str(e)}")
            raise

    def click(self, locator):
        try:

            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            sleep(1)
            element.click()
        except Exception as e:
            print(f"Failed to click element {locator}: {str(e)}")
            raise

    def find_element(self, locator, timeout=10):
        try:
            wait = self.long_wait if timeout == 20 else self.wait
            element = wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except TimeoutException:
            print(f"Element {locator} not found after {timeout} seconds")
            raise

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
            sleep(0.5)
            element.send_keys(text)
            sleep(0.5)
        except TimeoutException:
            print(f"Input field {locator} not found or not interactive")
            raise

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                element
            )
            sleep(1)
        except Exception as e:
            print(f"Failed to scroll to element: {str(e)}")
            raise

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


