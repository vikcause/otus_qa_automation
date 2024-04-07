"""
Fixtures for testing https://jsonplaceholde.typicode.com/
"""
import pytest
import requests


def pytest_addoption(parser):
    """parse method for cli"""

    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
        help="Requests base url"
    )


@pytest.fixture(scope="module")
def base_url(request):
    """fixture with main url"""

    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def session():
    """fixture create session"""

    return requests.Session()
