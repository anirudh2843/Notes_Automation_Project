import logging
import os
import sys


# Create logs folder
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{LOG_DIR}/Test.log"


# Configure logger
logger = logging.getLogger("FrameworkLogger")

logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# Clear old handlers
if logger.hasHandlers():
    logger.handlers.clear()


# File handler
file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")

# IMPORTANT FIX
console_handler = logging.StreamHandler(sys.stdout)


# Formatter
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

file_handler.setFormatter(formatter)

console_handler.setFormatter(formatter)


# Add handlers
logger.addHandler(file_handler)

logger.addHandler(console_handler)
