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
        # BrowserStack credentials
        bs_user = 'ianmckinney3'
        bs_key = 'xU4wgcY7j3HxeeYspEGs'

        # Create ChromeOptions instance for BrowserStack
        options = webdriver.ChromeOptions()

        # Set BrowserStack specific capabilities for mobile web testing
        browserstack_options = {
            # Device and OS settings
            'deviceName': 'Samsung Galaxy S22',
            'platformName': 'android',
            'platformVersion': '12.0',

            # Browser settings
            'browserName': 'chrome',  # or 'safari' for iOS devices

            # BrowserStack specific settings
            'local': 'false',
            'debug': 'true',
            'networkLogs': 'true',
            'projectName': 'Reelly Mobile Tests',
            'buildName': f'Build {scenario_name}',
            'sessionName': scenario_name,
            'interactiveDebugging': True,
            'acceptInsecureCerts': 'true',
            'consoleLogs': 'info'
        }

        options.set_capability('bstack:options', browserstack_options)

        # Initialize BrowserStack driver
        url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
        context.driver = webdriver.Remote(
            command_executor=url,
            options=options
        )



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