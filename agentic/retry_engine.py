import time

from utils.logger import logger


class RetryEngine:
    @staticmethod
    def execute(function, retries=2, delay=2):
        last_exception = None

        for attempt in range(retries + 1):
            try:
                if attempt == 0:
                    logger.info("Executing action")

                else:
                    logger.warning(f"Retry Attempt : {attempt}")

                return function()

            except Exception as e:
                last_exception = e

                logger.warning(f"Retry failed : {str(e)}")

                time.sleep(delay)

        raise last_exception
