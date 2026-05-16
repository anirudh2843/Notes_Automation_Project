import pytest

from pages.login_page import LoginPage


@pytest.mark.agentic
def test_ai_healing(driver):
    login_page = LoginPage(driver)

    # Open website
    driver.get("https://practice.expandtesting.com/notes/app")

    # Open login page
    login_page.go_to_login_page()

    login_page.password_input = ("id", "wrong_password")

    # Enter credentials
    login_page.send_keys(login_page.email_input, "dummy11@gmail.com")

    login_page.send_keys(login_page.password_input, "Dummy@123")

    # AI self-healing click
    login_page.click(login_page.login_btn)

    # FINAL ASSERTION
    assert login_page.is_login_successful(), (
        "AI self-healing failed to recover login button"
    )
