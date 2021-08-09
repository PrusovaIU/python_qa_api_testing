from help import check_get
from jsonschema import validate
import pytest


MESSAGE = "message"
STATUS = "status"

STATUS_OK = 200


@pytest.mark.parametrize("url",
                         [
                             pytest.param("https://dog.ceo/api/breeds/image/random", id="random_image"),
                             pytest.param("https://dog.ceo/api/breed/hound/images/random",
                                          id="random_image_from_a_breed_collection")
                         ])
def test_image(url: str):
    CONTENT_SCHEMA = {
        "type": "object",
        "properties": {
            MESSAGE: {"type": "string"},
            STATUS: {"type": "string"}
        }
    }
    EXPECTED_STATUS = "success"
    response = check_get(url, STATUS_OK)
    response_json = response.json()
    validate(response_json, CONTENT_SCHEMA)
    assert response_json.get(STATUS) == EXPECTED_STATUS, f"Unexpected status: \"{response_json.get(STATUS)}\". " \
                                                         f"\"{EXPECTED_STATUS}\" is expected"
    check_get(response_json.get(MESSAGE), STATUS_OK)



