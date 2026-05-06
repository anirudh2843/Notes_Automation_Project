import pytest
from utils.api_client import get_notes


@pytest.mark.api
def test_get_notes_response_time():
    response = get_notes()

    assert response.elapsed.total_seconds() < 2
