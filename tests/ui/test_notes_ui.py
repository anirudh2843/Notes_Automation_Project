import pytest
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.config_reader import Config
from mcp.llm_test_data_generator import LLMTestDataGenerator


@pytest.mark.regression
@pytest.mark.ui
def test_create_note_ui(driver):
    login = LoginPage(driver)
    login.login(Config.EMAIL, Config.PASSWORD)

    notes = NotesPage(driver)

    data = LLMTestDataGenerator.generate_note()

    title = data["title"]
    description = data["description"]
    category = data["category"]

    notes.create_note(title, description, category)

    assert notes.is_note_present(title)
