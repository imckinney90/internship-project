from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger
import os


def browser_init(context, scenario_name):
    """
    Initialize WebDriver instance for different test environments
    :param context: Behave context
    :param scenario_name: Name of the current scenario
    """

    # Read test configuration from environment variables
    test_env = os.getenv('TEST_ENV', 'browserstack')  # local, browserstack

    if test_env == 'browserstack':
        bs_user = 'ianmckinney3'
        bs_key = 'xU4wgcY7j3HxeeYspEGs'
        url = f'http://hub-cloud.browserstack.com/wd/hub'

        options = Options()
        bstack_options = {
            'deviceName': 'Samsung Galaxy S22 Ultra',  # Replace with desired device
            'platformName': 'Android',  # Or 'iOS'
            'browserName': 'Chrome',  # Mobile Chrome browser
            'sessionName': scenario_name,
            'interactiveDebugging': True
        }
        options.set_capability('bstack:options', bstack_options)
        options.set_capability('browserstack.user', bs_user)
        options.set_capability('browserstack.key', bs_key)
        context.driver = webdriver.Remote(command_executor=url, options=options)

    elif test_env == 'local':
        mobile_emulation = {
            "deviceName": "Nexus 5"
        }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument('--auto-open-devtools-for-tabs')

        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(
            service=service,
            options=options
        )

    elif test_env == 'grid':
        mobile_emulation = {"deviceName": "Nexus 5"}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.set_capability("browserName", "chrome")

        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            options=options
        )


    if test_env != 'browserstack':
        context.driver.set_window_size(360, 640)

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