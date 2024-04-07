"""
Fixtures for testing https://www.openbrewerydb.org/
"""
import pytest


@pytest.fixture()
def base_url():
    """fixture with main url"""

    return "https://api.openbrewerydb.org"
