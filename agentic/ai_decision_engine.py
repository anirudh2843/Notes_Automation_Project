from utils.logger import logger


class AIDecisionEngine:
    @staticmethod
    def should_retry(failure_type):
        retryable_failures = [
            "Locator Failure",
            "Synchronization Failure",
            "UI Overlay Issue",
        ]

        if failure_type in retryable_failures:
            logger.info(f"Retry approved for : {failure_type}")
            return True

        logger.error(f"Retry rejected for : {failure_type}")

        return False
