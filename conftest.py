import os
import pytest
import allure
from utils.logger import logger


pytest_plugins = ["fixtures.browser_fixture"]


# Test logs starts and ends
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    logger.info("-" * 50)
    logger.info(f"START TEST : {item.name}")
    logger.info("-" * 50)
    yield
    logger.info("-" * 50)
    logger.info(f"END TEST : {item.name}")
    logger.info("-" * 50)


# Failure Screenshot + Allure Attachment
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Capture only failed tests
    if report.when == "call" and report.failed:
        logger.error(f"TEST FAILED : {item.name}")

        driver = item.funcargs.get("driver")

        if driver:
            # Creating screenshots folder
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"

            # Save screenshot
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot captured : {screenshot_path}")

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
