import pytest

from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.config_reader import Config


@pytest.mark.regression
@pytest.mark.ui
def test_update_note_ui(driver):
    login = LoginPage(driver)

    login.login(Config.EMAIL, Config.PASSWORD)

    notes = NotesPage(driver)

    # Create Note
    notes.create_note("Old Note", "Old Description", "Home")

    # Click Edit
    notes.click_edit()

    # Update Note
    notes.update_note("Updated Note", "Updated Description")

    driver.refresh()

    # Validation
    assert notes.is_note_present("Updated Note")
