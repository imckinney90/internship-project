from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException


class OffPlanPage(BasePage):
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, "[class*='1-link-menu']")
    OFF_PLAN_TEXT = (By.XPATH, "//*[contains(@id, 'b528dfcf-d2ee-f936')]")
    PRODUCT_IMAGE = (By.CLASS_NAME, "project-image")
    PRODUCT_TITLE = (By.CLASS_NAME, "project-name")

    def navigate_to_off_plan(self):
        try:
            self.click(self.OFF_PLAN_BUTTON)
        except TimeoutException:
            raise TimeoutException("Off Plan button not clickable")

    def verify_off_plan_page(self):
        try:
            off_plan_text = self.find_element(self.OFF_PLAN_TEXT, timeout=20)
            return "Off-plan" in off_plan_text.text
        except TimeoutException:
            raise TimeoutException("Off Plan page text not found")

    def verify_products(self, expected_count=24):
        try:
            self.scroll_page_to_bottom()

            images = self.find_elements(self.PRODUCT_IMAGE, timeout=20)
            titles = self.find_elements(self.PRODUCT_TITLE, timeout=20)

            if len(images) != expected_count or len(titles) != expected_count:
                raise AssertionError(
                    f"Expected {expected_count} products, but found {len(images)} images and {len(titles)} titles"
                )

            for index, (image, title) in enumerate(zip(images, titles), 1):
                self.scroll_to_element(image)

                if not image.is_displayed():
                    raise ElementNotVisibleException(f"Image #{index} not displayed")
                if not title.is_displayed():
                    raise ElementNotVisibleException(f"Title #{index} not displayed")

            return True

        except Exception as e:
            raise Exception(f"Product verification failed: {str(e)}")

