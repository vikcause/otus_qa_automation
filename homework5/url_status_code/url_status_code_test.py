"""
module for testing reading url and check required status_code
"""
import requests


def test_response_status(url, expected_status_code):
    """method to check url and status_code"""

    response = requests.get(url, timeout=10)
    actual_status_code = response.status_code
    assert actual_status_code == expected_status_code, \
        (f"Actual {actual_status_code} and expected {expected_status_code} "
         f"status code not equal")
