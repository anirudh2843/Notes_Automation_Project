from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import retry
from utils.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        def action():
            logger.info(f"Clicking  : {locator}")

            element = self.wait.until(EC.element_to_be_clickable(locator))

            # Scroll element into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )

            # Wait for page stabilization
            self.wait.until(EC.element_to_be_clickable(locator))

            try:
                element.click()
                logger.info(f"Successfully clicked : {locator}")
            except:
                logger.warning(f"Normal click failed. Using JS click : {locator}")
                # Fallback JS click
                self.driver.execute_script("arguments[0].click();", element)

        retry(action)

    def send_keys(self, locator, value):
        logger.info(f"Entering text '{value}' into : {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        logger.info(f"Getting text from : {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        logger.info(f"Retrieved text from {locator}: {element.text}")
        return element.text

    def refresh_page(self):
        logger.info("Refreshing page")
        self.driver.refresh()
