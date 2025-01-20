from sys import excepthook

from django.db.models import EmailField
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = (By.ID, "email-2")
PASSWORD = (By.ID, "field")
LOGIN =  (By.CSS_SELECTOR, "[wized='loginButton']")

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