import requests
from config.config_reader import Config
from utils.logger import logger


def get_token():
    logger.info("Generating API token")
    url = f"{Config.API_URL}/users/login"

    payload = {"email": Config.EMAIL, "password": Config.PASSWORD}

    response = requests.post(url, json=payload)
    logger.info(f"Login API Status Code : {response.status_code}")

    token = response.json()["data"]["token"]

    logger.info("Token generated successfully")

    return token


def get_headers():
    return {"x-auth-token": get_token()}


def get_notes():
    logger.info("Calling GET /notes API")

    response = requests.get(f"{Config.API_URL}/notes", headers=get_headers())

    logger.info(f"GET /notes Response Code : {response.status_code}")

    return response


def delete_note(note_id):
    logger.info(f"Deleting note using API : {note_id}")

    response = requests.delete(
        f"{Config.API_URL}/notes/{note_id}", headers=get_headers()
    )

    logger.info(f"DELETE API Response Code : {response.status_code}")
    return response


def get_notes_invalid_token():
    logger.info("Calling GET /notes with invalid token")

    headers = {"x-auth-token": "invalid_token"}

    response = requests.get(f"{Config.API_URL}/notes", headers=headers)

    logger.info(f"Invalid Token Response : {response.status_code}")

    return response


def login_missing_fields():
    logger.info("Calling login API with missing fields")

    payload = {"email": ""}

    response = requests.post(f"{Config.API_URL}/users/login", json=payload)

    logger.info(f"Missing Fields Response : {response.status_code}")

    return response
