import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_URL = os.getenv("API_URL")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    BROWSER = os.getenv("BROWSER", "chrome")
    EXECUTION_ENV = os.getenv("EXECUTION_ENV", "local")
    GRID_URL = os.getenv("GRID_URL")
