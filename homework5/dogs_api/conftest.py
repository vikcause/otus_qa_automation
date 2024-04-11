"""
Fixtures for testing https://dog.ceo/dog-api
"""
import pytest


@pytest.fixture()
def base_url():
    """fixture with main url"""

    return "https://dog.ceo/api"


@pytest.fixture()
def get_random_image():
    """fixture for getting random image"""

    return "breeds/image/random"
