from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find_element(self, locator, timeout=10):
        wait = self.long_wait if timeout == 20 else self.wait
        return wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        wait = self.long_wait if timeout == 20 else self.wait
        return wait.until(EC.presence_of_all_elements_located(locator))

    def input_text(self, text, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -100);")
        sleep(1)

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


