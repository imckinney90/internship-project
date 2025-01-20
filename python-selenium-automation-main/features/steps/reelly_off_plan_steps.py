from sys import excepthook

from django.db.models import EmailField
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


Off_Plan_Button = (By.CSS_SELECTOR, "[class*='1-link-menu']")
Off_Plan_Text = (By.XPATH, "//*[contains(@id, 'b528dfcf-d2ee-f936')]")
Product_Image = (By.CLASS_NAME, "project-image")
Product_Title = (By.CLASS_NAME, "project-name")


@when('Navigate to the "Off plan" page via the left-side menu')
def navigate_to_off_plan(context):
    off_plan_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='1-link-menu']"))
    )
    off_plan_button.click()


@then('Verify the "Off plan" page is displayed')
def verify_off_plan(context):
    off_plan_text = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'b528dfcf-d2ee-f936')]"))
    )

    assert "Off-plan" in off_plan_text.text, f'Expected text "Off-plan" but found "{off_plan_text.text}"'


@then('Verify each product contains a visible title and picture')
def verify_visible_product(context):
    last_height = context.driver.execute_script("return document.body.scrollHeight")

    while True:
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        new_height = context.driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    context.driver.execute_script("window.scrollTo(0, 0);")


    images = WebDriverWait(context.driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "project-image"))
    )
    titles = WebDriverWait(context.driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "project-name"))
    )

    assert len(images) == len(
        titles) == 24, f"Expected 24 products, but found {len(images)} images and {len(titles)} titles"

    for index, (image, title) in enumerate(zip(images, titles), 1):
        try:

            context.driver.execute_script("arguments[0].scrollIntoView(true);", image)
            context.driver.execute_script("window.scrollBy(0, -100);")
            sleep(1)


            assert image.is_displayed(), f"Image #{index} with class 'project-image' is not displayed"
            assert title.is_displayed(), f"Title #{index} with class 'project-name' is not displayed"

            print(f"Product #{index}: Image and title are visible")

        except Exception as e:
            assert False, f"Failed to verify product #{index}: {str(e)}"

    print(f"Successfully verified all {len(images)} products have visible images and titles")


