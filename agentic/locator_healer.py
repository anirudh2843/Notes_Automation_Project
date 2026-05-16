import ast

from selenium.webdriver.common.by import By

from mcp.llm_locator_suggester import LLMLocatorSuggestor

from utils.logger import logger


class LocatorHealer:
    @staticmethod
    def heal(driver, locator):
        logger.warning(f"Trying to heal locator : {locator}")

        page_source = driver.page_source

        suggestions = LLMLocatorSuggestor.suggest_locator(locator, page_source)

        logger.warning(f"LLM Locator Suggestions : {suggestions}")

        try:
            suggestions = ast.literal_eval(suggestions)

        except Exception:
            suggestions = []

        for xpath in suggestions:
            try:
                element = driver.find_element(By.XPATH, xpath)

                logger.info(f"Recovered using AI locator : {xpath}")

                return element

            except Exception:
                continue

        raise Exception(f"Unable to heal locator : {locator}")
