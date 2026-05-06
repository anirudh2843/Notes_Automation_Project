import pytest
from utils.api_client import get_notes


@pytest.mark.api
def test_get_notes():
    response = get_notes()
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
