from pages.login_page import LoginPage


def test_ai_failure(driver):
    login_page = LoginPage(driver)

    # Open website
    driver.get("https://practice.expandtesting.com/notes/app")

    # Open login page
    login_page.go_to_login_page()

    # Enter credentials
    login_page.send_keys(login_page.email_input, "dummy11@gmail.com")

    login_page.send_keys(login_page.password_input, "Dummy@123")

    # BREAK ONLY LOGIN BUTTON
    login_page.login_btn = ("id", "wrong_locator")

    # Now AI healing should happen
    login_page.click(login_page.login_btn)
