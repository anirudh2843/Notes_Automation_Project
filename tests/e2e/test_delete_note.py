import pytest

from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.api_client import get_notes, delete_note
from config.config_reader import Config


@pytest.mark.e2e
@pytest.mark.regression
def test_api_to_ui_delete_sync(driver):
    login = LoginPage(driver)

    login.login(Config.EMAIL, Config.PASSWORD)

    notes = NotesPage(driver)

    title = "Delete Me"
    description = "To be deleted"
    category = "Home"

    notes.create_note(title, description, category)

    assert notes.is_note_present(title)

    response = get_notes()

    data = response.json()["data"]

    note_id = None

    for note in data:
        if note["title"] == title:
            note_id = note["id"]

            break

    assert note_id is not None

    delete_response = delete_note(note_id)

    assert delete_response.status_code in [200, 204]

    updated_notes = get_notes().json()["data"]

    assert not any(note["id"] == note_id for note in updated_notes)

    notes.refresh_page()

    titles = notes.get_all_titles()

    assert title not in titles

    assert all(t.strip() != "" for t in titles)
