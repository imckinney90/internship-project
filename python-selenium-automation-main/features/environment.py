from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def before_all(context):
    init_driver(context)


def init_driver(context):
    logger.info("Initializing chrome driver")

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")  # Enabled headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())

    try:
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        context.app = Application(context.driver)
        logger.info("Chrome driver setup completed")
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