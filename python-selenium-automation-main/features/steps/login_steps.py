from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@given('Log in with valid credentials')
def login_with_valid_credentials(context):
    context.app.login_page.login()

@given('Log in with valid credentials for web')
def login_with_valid_credentials_for_web(context):
    context.app.login_page.login_mobile_web()

