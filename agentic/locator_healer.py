from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger
from mcp.llm_locator_suggester import LLMLocatorSuggester


class LocatorHealer:
    @staticmethod
    def heal(driver, locator):
        logger.warning(f"Trying to heal locator : {locator}")

        suggestions = LLMLocatorSuggester.suggest(locator)

        logger.warning(f"LLM Locator Suggestions : {suggestions}")

        by, value = locator

        possible_locators = []

        # LOGIN / CREATE BUTTONS
        if "button" in value.lower():
            possible_locators = [
                (By.XPATH, "//button[contains(text(),'Login')]"),
                (By.XPATH, "//button[contains(text(),'Create')]"),
                (By.XPATH, "//button[@type='submit']"),
            ]

        # TITLE INPUT
        elif "title" in value.lower():
            possible_locators = [
                (By.ID, "title"),
                (By.NAME, "title"),
                (By.XPATH, "//input[@id='title']"),
            ]

        # DESCRIPTION INPUT
        elif "description" in value.lower():
            possible_locators = [(By.ID, "description"), (By.NAME, "description")]

        for new_locator in possible_locators:
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(new_locator)
                )

                logger.info(f"Healed locator success : {new_locator}")

                return element

            except Exception:
                continue

        raise Exception(f"Unable to heal locator : {locator}")
