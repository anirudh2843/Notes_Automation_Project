import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.config_reader import Config
from utils.logger import logger


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())

    if Config.EXECUTION_ENV == "grid":
        logger.info("Running tests on Selenium Grid")
        driver = webdriver.Remote(command_executor=Config.GRID_URL, options=options)
    else:
        logger.info("Running tests locally")
        driver = webdriver.Chrome(service=service, options=options)

    driver.get(Config.BASE_URL)

    yield driver
    driver.quit()
