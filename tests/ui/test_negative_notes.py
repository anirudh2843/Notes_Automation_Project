import pytest
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.config_reader import Config


@pytest.mark.ui
@pytest.mark.negative
def test_create_note_empty_title(driver):
    # Login
    login = LoginPage(driver)
    login.login(Config.EMAIL, Config.PASSWORD)

    # Open notes page
    notes = NotesPage(driver)

    # Open create modal
    notes.click(notes.add_btn)

    # Enter only description
    notes.send_keys(notes.desc_input, "Testing empty title validation")

    # Click Create
    notes.click(notes.create_btn)

    # Validate error message
    assert notes.is_title_required_error_displayed(), (
        "Title required validation not displayed"
    )
