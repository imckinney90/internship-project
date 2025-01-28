from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application
from support.logger import logger

# Commands to run tests with Allure & Behave:
# behave
# behave features/tests/cart_tests.feature
# behave -t smoke
#
# # After you have Allure installed:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ -t smoke
#
# # To generate the report:
# allure serve test_results/

def browser_init(context, scenario_name):
    """
    Initialize WebDriver instance for Headless Chrome
    :param context: Behave context
    :param scenario_name: Name of the current scenario
    """
    ### HEADLESS CHROME ###
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )

    # Set up window and wait times
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario:{scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}:')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'Step failed: {step}:')

def after_scenario(context, feature):
    context.driver.quit()