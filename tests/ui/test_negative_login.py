import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.parametrize(
    "email, password",
    [
        ("wrong@gmail.com", "Dummy@123"),
        ("dummy11@gmail.com", "wrongpassword"),
        ("", "Dummy@123"),
        ("dummy11@gmail.com", ""),
        ("", ""),
    ],
)
def test_login_invalid_credentials(driver, email, password):
    login = LoginPage(driver)

    login.login(email, password)

    assert not login.is_login_successful(), "Login should fail for invalid credentials"
