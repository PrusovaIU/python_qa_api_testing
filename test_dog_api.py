from help import check_get
from jsonschema import validate


MESSAGE = "message"
STATUS = "status"

STATUS_OK = 200


def test_random_image():
    CONTENT_SCHEMA = {
        "type": "object",
        "properties": {
            MESSAGE: {"type": "string"},
            STATUS: {"type": "string"}
        }
    }
    EXPECTED_STATUS = "success"
    response = check_get("https://dog.ceo/api/breeds/image/random", STATUS_OK)
    response_json = response.json()
    validate(response_json, CONTENT_SCHEMA)
    assert response_json.get(STATUS) == EXPECTED_STATUS, f"Unexpected status: \"{response_json.get(STATUS)}\". " \
                                                         f"\"{EXPECTED_STATUS}\" is expected"
    check_get(response_json.get(MESSAGE), STATUS_OK)
