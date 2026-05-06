import pytest

from pages.login_page import LoginPage
from config.config_reader import Config


@pytest.mark.smoke
@pytest.mark.ui
def test_login_success(driver):
    login = LoginPage(driver)
    login.login(Config.EMAIL, Config.PASSWORD)

    assert login.is_login_successful(), "Login failed"
