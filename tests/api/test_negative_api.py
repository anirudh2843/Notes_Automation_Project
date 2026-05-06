import pytest
import requests
from utils.api_client import get_notes_invalid_token, login_missing_fields
from config.config_reader import Config

@pytest.mark.api
@pytest.mark.negative
def test_api_invalid_token():
    response = get_notes_invalid_token()

    assert response.status_code == 401


def test_api_login_missing_fields():
    response = login_missing_fields()

    assert response.status_code in [400, 401]


def test_api_invalid_endpoint():
    response = requests.get(f"{Config.API_URL}/invalid_endpoint")

    assert response.status_code == 404
