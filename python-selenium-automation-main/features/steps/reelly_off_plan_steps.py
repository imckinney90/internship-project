from sys import excepthook

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('Log in with valid credentials')
def login_with_valid_credentials(context):  # Added function definition
    email_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email-2"))
    )
    email_field.send_keys("reelly_careerist_test@proton.me")
    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "field"))
    )
    password_field.send_keys("Test")
    continue_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[wized='loginButton']"))
    )
    continue_button.click()


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

    assert len(images) == 24, f"Expected 24 project images, but found {len(images)}"

    for index, image in enumerate(images, 1):
        try:
            context.driver.execute_script("arguments[0].scrollIntoView(true);", image)
            context.driver.execute_script("window.scrollBy(0, -100);")

            assert image.is_displayed(), f"Image #{index} with class 'project-image' is not displayed"
            print(f"Image #{index} is visible")

        except Exception as e:
            assert False, f"Failed to verify visibility of image #{index}: {str(e)}"

    print(f"Successfully verified all {len(images)} project images are present and visible")
