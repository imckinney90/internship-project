from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger(__name__)


class MainPage(BasePage):
    BASE_URL = 'https://soft.reelly.io/'

    def open_main(self):
        logger.info(f"Attempting to open URL: {self.BASE_URL}")
        try:
            self.driver.get(self.BASE_URL)
            logger.info("URL opened, waiting for page load")


            self.wait.until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            logger.info("Page load complete")


            current_url = self.driver.current_url
            logger.info(f"Current URL: {current_url}")

            if not current_url.startswith(self.BASE_URL):
                raise Exception(f"Expected URL to start with {self.BASE_URL}, but got {current_url}")

        except Exception as e:
            logger.error(f"Failed to open main page: {str(e)}")
            raise


