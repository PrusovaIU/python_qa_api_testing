from typing import Optional
import requests


def check_get(url: str, status_code: int, params: dict = None) -> Optional[requests.Response]:
    response = requests.get(url, params)
    assert response.status_code == status_code, f"{url}: wrong status code \"{response.status_code}\"." \
                                                f"\"{status_code}\" is expected."
    return response
