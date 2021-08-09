from help import check_get
from jsonschema import validate
from requests import Response
from typing import Optional
import pytest


MESSAGE = "message"
STATUS = "status"

EXPECTED_MES_STATUS = "success"

STATUS_OK = 200

CONTENT_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        MESSAGE: {
            "type": "array",
            "items": {"type": "string"}
        },
        STATUS: {"type": "string"}
    }
}


def check_response(url: str, content_schema: dict) -> Optional[Response]:
    response = check_get(url, STATUS_OK)
    response_json = response.json()
    validate(response_json, content_schema)
    assert response_json.get(STATUS) == EXPECTED_MES_STATUS, f"Unexpected status: \"{response_json.get(STATUS)}\". " \
                                                             f"\"{EXPECTED_MES_STATUS}\" is expected"
    return response


@pytest.mark.parametrize("url",
                         [
                             pytest.param("https://dog.ceo/api/breeds/image/random", id="random_image"),
                             pytest.param("https://dog.ceo/api/breed/hound/images/random",
                                          id="random_image_from_a_breed_collection"),
                             pytest.param("https://dog.ceo/api/breed/hound/afghan/images/random",
                                          id="single_random_image_from_a_sub_breed_collection")
                         ])
def test_image(url: str):
    CONTENT_SCHEMA = {
        "type": "object",
        "properties": {
            MESSAGE: {"type": "string"},
            STATUS: {"type": "string"}
        }
    }
    response = check_response(url, CONTENT_SCHEMA)
    check_get(response.json().get(MESSAGE), STATUS_OK)


@pytest.mark.parametrize("url",
                         [
                             pytest.param("https://dog.ceo/api/breed/hound/images", id="by_breed"),
                             pytest.param("https://dog.ceo/api/breed/hound/list", id="list_all_sub_breeds")
                         ])
def test_get_list(url: str):
    check_response(url, CONTENT_LIST_SCHEMA)
