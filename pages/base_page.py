from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
)
from mcp.llm_failure_analyzer import LLMFailureAnalyzer

from utils.logger import logger

from agentic.locator_healer import LocatorHealer
from agentic.retry_engine import RetryEngine
from agentic.failure_analyzer import FailureAnalyzer
from agentic.ai_decision_engine import AIDecisionEngine
from agentic.intelligent_wait import IntelligentWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        def action():
            logger.info(f"Clicking : {locator}")

            try:
                element = IntelligentWait.wait_for_clickable(self.driver, locator)

            except Exception:
                logger.warning(f"Locator failed. Trying self healing : {locator}")

                element = LocatorHealer.heal(self.driver, locator)

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )

            try:
                element.click()

                logger.info("Successfully clicked")

            except ElementClickInterceptedException:
                logger.info(f"Recovered using JS click : {locator}")

                self.driver.execute_script("arguments[0].click();", element)

        try:
            RetryEngine.execute(action)

        except Exception as e:
            failure_type = FailureAnalyzer.analyze(e)
            logger.error(f"Failure Type : {failure_type}")

            # MCP LLM Analysis
            llm_analysis = LLMFailureAnalyzer.analyze(e)

            logger.error(f"LLM Analysis : {llm_analysis}")

            if AIDecisionEngine.should_retry(failure_type):
                logger.info("AI Retry Triggered")

                RetryEngine.execute(action)

            else:
                raise e

                

    def send_keys(self, locator, value):
        logger.info(f"Entering text '{value}' into : {locator}")

        try:
            element = IntelligentWait.wait_for_visible(self.driver, locator)

        except Exception:
            logger.warning(f"Self healing send_keys locator : {locator}")

            element = LocatorHealer.heal(self.driver, locator)

        element.clear()

        element.send_keys(value)




    def get_text(self, locator):
        logger.info(f"Getting text from : {locator}")

        element = IntelligentWait.wait_for_visible(self.driver, locator)

        logger.info(f"Retrieved text from {locator}: {element.text}")

        return element.text
    


    def refresh_page(self):
        logger.info("Refreshing page")

        self.driver.refresh()
