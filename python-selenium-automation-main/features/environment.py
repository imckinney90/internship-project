from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def before_all(context):
    init_driver(context)


def init_driver(context):
    # Determine which browser to use (default to Chrome can change to Firefox)
    browser = context.config.userdata.get('browser', 'Chrome').lower()

    if browser == 'chrome':
        logger.info("Initializing Chrome driver")
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")  # Enabled headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService(ChromeDriverManager().install())

        try:
            context.driver = webdriver.Chrome(service=service, options=chrome_options)
            logger.info("Chrome driver initialized successfully")
        except Exception as e:
            logger.error(f"Chrome driver setup failed: {str(e)}")
            raise

    elif browser == 'firefox':
        logger.info("Initializing Firefox driver")
        firefox_options = FirefoxOptions()

        # Firefox-specific settings
        firefox_options.add_argument("--headless")
        firefox_options.set_preference("browser.link.open_newwindow", 3)
        firefox_options.set_preference("browser.sessionstore.resume_from_crash", False)
        firefox_options.set_preference("network.http.connection-timeout", 60000)
        firefox_options.set_preference("dom.disable_beforeunload", True)
        firefox_options.set_preference("browser.tabs.remote.autostart", False)
        firefox_options.set_preference("browser.sessionhistory.max_total_viewers", 0)
        firefox_options.set_preference("dom.webdriver.enabled", True)
        firefox_options.set_preference("marionette.enabled", True)

        service = FirefoxService(GeckoDriverManager().install())

        try:
            context.driver = webdriver.Firefox(service=service, options=firefox_options)
            logger.info("Firefox driver initialized successfully")
        except Exception as e:
            logger.error(f"Firefox driver setup failed: {str(e)}")
            raise

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        context.app = Application(context.driver)
        logger.info(f"{browser} driver setup completed")
    except Exception as e:
        logger.error(f"Driver setup failed: {str(e)}")
        raise


def before_scenario(context, scenario):
    logger.info(f"Starting scenario: {scenario.name}")


def after_scenario(context, scenario):
    logger.info(f"Completing scenario: {scenario.name}")
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()