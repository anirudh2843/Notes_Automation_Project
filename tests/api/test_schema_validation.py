import pytest
from utils.api_client import get_notes


@pytest.mark.api
def test_note_schema_validation():
    response = get_notes()

    notes = response.json()["data"]

    if notes:
        note = notes[0]

        assert "id" in note
        assert "title" in note
        assert "description" in note
        assert "category" in note
