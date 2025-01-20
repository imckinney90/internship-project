from sys import excepthook

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
    context.app.offplan_page.navigate_to_off_plan()


@then('Verify the "Off plan" page is displayed')
def verify_off_plan(context):
    assert context.app.offplan_page.verify_off_plan_page(), \
        "Off-plan page text not found or incorrect"



@then('Verify each product contains a visible title and picture')
def verify_visible_product(context):
    assert context.app.offplan_page.verify_products(), \
        "Product verification failed"


