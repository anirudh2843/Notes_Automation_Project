from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)


class FailureAnalyzer:
    @staticmethod
    def analyze(exception):
        if isinstance(exception, NoSuchElementException):
            return "Locator Failure"

        if isinstance(exception, TimeoutException):
            return "Synchronization Failure"

        if isinstance(exception, ElementClickInterceptedException):
            return "Click Intercepted"

        return "Unknown Failure"
