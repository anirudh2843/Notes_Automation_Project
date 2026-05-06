import pytest
from utils.api_client import get_notes, delete_note


@pytest.mark.api
def test_delete_note_api():
    response = get_notes()

    notes = response.json()["data"]

    if notes:
        note_id = notes[0]["id"]

        delete_response = delete_note(note_id)

        assert delete_response.status_code in [200, 204]
