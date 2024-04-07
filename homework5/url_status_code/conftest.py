"""
Fixtures for testing url status code
"""
import pytest


@pytest.fixture(scope="session")
def url(request):
    """fixture for reading required url"""

    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def expected_status_code(request):
    """fixture for reading required status_code"""

    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    """method to work with CLI"""

    parser.addoption("--url", action="store", default="https://ya.ru",
                     help="Url for test")
    parser.addoption("--status_code", action="store", default="200",
                     type=int, help="required status code")
