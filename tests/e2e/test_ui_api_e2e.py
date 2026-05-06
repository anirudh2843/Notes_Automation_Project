import pytest

from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.api_client import get_notes
from config.config_reader import Config

@pytest.mark.e2e
@pytest.mark.regression
def test_ui_to_api_consistency(driver):
    login = LoginPage(driver)

    login.login(Config.EMAIL, Config.PASSWORD)

    notes = NotesPage(driver)

    title = "E2E Note"
    description = "UI API validation"
    category = "Home"

    notes.create_note(title, description, category)

    assert notes.is_note_present(title)

    response = get_notes()

    assert response.status_code == 200

    assert response.elapsed.total_seconds() < 2

    data = response.json()["data"]

    found = any(
        note["title"] == title
        and note["description"] == description
        and note["category"] == category
        for note in data
    )

    assert found
