import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.config_reader import Config


@pytest.fixture
def driver():
    options = Options() 
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(Config.BASE_URL)

    yield driver
    driver.quit()